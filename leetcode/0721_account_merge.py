"""
"""

import os, sys, shutil
from collections import defaultdict, Counter
import pdb


class Solution(object):
    def accountsMerge(self, accounts):
        # init
        id2name = dict()
        email2id = dict()
        id2emails = defaultdict(list)
        idx = 0

        for info in accounts:
            name = info[0]
            emails = info[1:]

            dup_ids = set()
            for email in emails:
                if email in email2id:
                    dup_id = email2id[email]
                    dup_ids.add(dup_id)

            if len(dup_ids) > 0:
                # merge duplicate idx and re-order them to a new id
                for dup_id in dup_ids: 
                    for email in id2emails[dup_id]:
                        email2id[email] = idx
                        id2emails[idx].append(email)
                # remove old ids
                for dup_id in dup_ids:
                    del id2emails[dup_id]
                # update emails
                for email in emails:
                    if email not in email2id:
                        email2id[email] = idx
                        id2emails[idx].append(email)
            # new accounts
            else: 
                for email in emails:
                    if email not in email2id:
                        email2id[email] = idx
                        id2emails[idx].append(email)
            # update idx
            id2name[idx] = name
            idx += 1
        
        res = list()
        for idx in id2emails:
            name = id2name[idx]
            emails = sorted(id2emails[idx])
            res.append([name,] + emails)
        return res


def main():
    """
    accounts = [
            ["John","johnsmith@mail.com","john_newyork@mail.com"],
            ["John","johnsmith@mail.com","john00@mail.com"],
            ["Mary","mary@mail.com"],
            ["John","johnnybravo@mail.com"]]
    accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
    """

    """
    accounts = [["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]
    """

    accounts = [["Alex","Alex5@m.co","Alex4@m.co","Alex0@m.co"],["Ethan","Ethan3@m.co","Ethan3@m.co","Ethan0@m.co"],["Kevin","Kevin4@m.co","Kevin2@m.co","Kevin2@m.co"],["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe2@m.co"],["Gabe","Gabe3@m.co","Gabe4@m.co","Gabe2@m.co"]]



    sol = Solution()
    res = sol.accountsMerge(accounts)

    for account in res:
        print(account)


if __name__ == '__main__':
    main()
