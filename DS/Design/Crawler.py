# 1236. Web Crawler
# Medium

# Given a url startUrl and an interface HtmlParser, implement a web crawler to crawl all links that are under the same hostname as startUrl.

# Return all urls obtained by your web crawler in any order.

# Your crawler should:

# Start from the page: startUrl
# Call HtmlParser.getUrls(url) to get all urls from a webpage of given url.
# Do not crawl the same link twice.
# Explore only the links that are under the same hostname as startUrl.


# As shown in the example url above, the hostname is example.org. For simplicity sake, you may assume all urls use http protocol without any port specified. For example, the urls http://leetcode.com/problems and http://leetcode.com/contest are under the same hostname, while urls http://example.org/test and http://example.com/abc are not under the same hostname.

# The HtmlParser interface is defined as such:

# interface HtmlParser {
#   // Return a list of all urls from a webpage of given url.
#   public List<String> getUrls(String url);
# }

# Example 1:

# Input:
# urls = [
#   "http://news.yahoo.com",
#   "http://news.yahoo.com/news",
#   "http://news.yahoo.com/news/topics/",
#   "http://news.google.com",
#   "http://news.yahoo.com/us"
# ]
# edges = [[2,0],[2,1],[3,2],[3,1],[0,4]]
# startUrl = "http://news.yahoo.com/news/topics/"
# Output: [
#   "http://news.yahoo.com",
#   "http://news.yahoo.com/news",
#   "http://news.yahoo.com/news/topics/",
#   "http://news.yahoo.com/us"
# ]
# Example 2:

# Input:
# urls = [
#   "http://news.yahoo.com",
#   "http://news.yahoo.com/news",
#   "http://news.yahoo.com/news/topics/",
#   "http://news.google.com"
# ]
# edges = [[0,2],[2,1],[3,2],[3,1],[3,0]]
# startUrl = "http://news.google.com"
# Output: ["http://news.google.com"]
# Explanation: The startUrl links to all other pages that do not share the same hostname.

# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
# class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution(object):
    def crawl(self, startUrl, htmlParser):
        """
        :type startUrl: str
        :type htmlParser: HtmlParser
        :rtype: List[str]
        """
        visited = set()
        frontier = collections.deque()
        domain = startUrl.split("http://")[1].split("/")[0]
        result = [startUrl]

        # Put the seed url in the frontier and mark it as visited
        frontier.append(startUrl)
        visited.add(startUrl)

        # BFS
        while frontier:
            curr = frontier.popleft()
            next_set = htmlParser.getUrls(curr)
            for url in next_set:
                if url.split("http://")[1].split("/")[0] != domain or url in visited:
                    continue
                else:
                    frontier.append(url)
                    result.append(url)
                    visited.add(url)
        return result
