# import pdb
import torch
import torch.nn as nn
import torch.nn.functional as F
from self_attn_ref import MultiHeadAttentionRef


class MultiHeadAttention(nn.Module):
    """
    An implementation of a Multi-Head Attention layer.
    """
    def __init__(self, embed_dim, num_heads):
        """
        Args:
            embed_dim (int): The dimensionality of the input embedding.
            num_heads (int): The number of attention heads.
        """
        super(MultiHeadAttention, self).__init__()
        self.embed_dim = embed_dim
        self.num_heads = num_heads
        
        # The dimension of each head's query, key, and value vectors
        self.head_dim = embed_dim // num_heads
        
        # Ensure that embed_dim is divisible by num_heads
        assert (
            self.head_dim * num_heads == embed_dim
        ), "Embedding size needs to be divisible by the number of heads."
        
        # Linear layers for Q, K, V projections.
        # We can do this in one pass for efficiency.
        self.qkv_layer = nn.Linear(embed_dim, 3 * embed_dim)
        
        # Final linear layer after concatenating the heads
        # self.fc_out = nn.Linear(embed_dim, embed_dim)


    def forward(self, x, mask=None):
        """
        Args:
            x (torch.Tensor): The input tensor of shape (batch_size, seq_len, embed_dim).
            mask (torch.Tensor, optional): A mask to prevent attention to certain positions
        Returns:
            torch.Tensor: The output tensor of shape (batch_size, seq_len, embed_dim).
        """
        N, seq_len, _ = x.shape
        
        # x: (batch_size, seq_len, embed_dim) -> q, k, v: (batch_size, seq_len, embed_dim)
        qkv = self.qkv_layer(x)
        q, k, v = qkv.chunk(3, dim=-1)
        
        # 2. Split the combined qkv into separate Q, K, V
        # qkv: (batch_size, seq_len, 3 * embed_dim) -> Q, K, V: (batch_size, seq_len, embed_dim) each
        # queries, keys, values = qkv.chunk(3, dim=-1)
        
        # 3. Reshape for multi-head processing
        q = q.reshape(N, seq_len, self.num_heads, self.head_dim)
        k = k.reshape(N, seq_len, self.num_heads, self.head_dim)
        v = v.reshape(N, seq_len, self.num_heads, self.head_dim)

        # (n, seq_len, num_heads, head_dim) -> (n, num_heads, seq_len, head_dim)
        q = q.transpose(1, 2)
        k = k.transpose(1, 2)
        v = v.transpose(1, 2)

        # score: (N, num_heads, seq_len, seq_len)
        scores = q @ k.transpose(-1, -2) / (self.head_dim ** 0.5)
        # Another implementation of scores
        # it may be better as q and k may be close to float upperbond, divide them first can prevent overflow
        # however, gemini does not think so
        # norm_term = self.head_dim ** 0.25
        # scores = (q / norm_term) @ (k.transpose(-1, -2) / norm_term)
        
        # Apply mask if provided
        if mask is not None:
            scores = scores.masked_fill(mask == 0, float("-1e9"))
            
        # score: (N, num_heads, seq_len, seq_len)
        scores = F.softmax(scores, dim=-1)
        
        # score: (N, num_heads, seq_len, head_dim)
        output = torch.matmul(scores, v)
        
        # (N, num_heads, seq_len, head_dim) -> (N, seq_len, num_heads, head_dim)
        # (N, seq_len, num_heads, head_dim) -> (N, seq_len, num_heads * head_dim)
        output = output.transpose(1, 2).reshape(N, seq_len, self.embed_dim)
        
        return output


def main():
    # --- Configuration ---
    batch_size = 1
    seq_len = 5
    embed_dim = 256  # Total embedding dimension
    num_heads = 8     # Number of parallel attention heads

    # --- Model & Input ---
    model_ref = MultiHeadAttentionRef(embed_dim, num_heads)
    model = MultiHeadAttention(embed_dim, num_heads)

    model.load_state_dict(model_ref.state_dict())

    # Create a random input tensor
    # Shape: (batch_size, seq_len, embed_dim)
    input_tensor = torch.rand(batch_size, seq_len, embed_dim)

    # --- Forward Pass ---
    output_ref = model_ref(input_tensor)
    output = model(input_tensor)

    diff = output_ref - output
    print(diff.abs())
    print(diff.abs().max())

    # --- Check Output ---
    # print("Input Shape:", input_tensor.shape)
    # print("Output Shape:", output_tensor.shape)


if __name__ == '__main__':
    main()