class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ans = set()
        for email in emails:
            local = email[:email.index('@')]
            domain = email[email.index('@')+1:]
            if '+' in local:
                local = local[:local.index('+')]
            local = local.replace('.', '')
            ans.add(local+'@'+domain)
        return len(ans)