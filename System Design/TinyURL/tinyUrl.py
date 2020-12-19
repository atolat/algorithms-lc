# 535. Encode and Decode TinyURL
# Medium

# Note: This is a companion problem to the System Design problem: Design TinyURL.
# TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

# Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

class Codec:
    def __init__(self):
        # Maintain a global counter
        self.counter = 0

        # Dictionary represents - Database/Cache
        self.db = collections.defaultdict(str)

        # base 64 encoding
        self.b64 = string.ascii_letters + string.digits + '_-'

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        # Increment counter
        self.counter += 1

        # Base 64 encoding
        currval = self.counter
        enc_64 = collections.deque()
        while currval >= 64:
            quotient = currval//64
            remainder = currval % 64
            enc_64.appendleft(self.b64[remainder])
            currval = quotient
        if currval > 0:
            enc_64.appendleft(self.b64[currval])

        # Fill in the encoded string with a till the length is 7
        while len(enc_64) < 7:
            enc_64.appendleft('a')

        back = ''.join(enc_64)

        # Make an entry in DB
        self.db[back] = longUrl

        return 'https://tinyurl.com/'+back

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        # Extract encoded string and retureve it from db
        back = shortUrl.split('/')[-1]
        return self.db[back]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
