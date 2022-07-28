class Solution:
   def solve(self, book, page, page_size):
      l=page*page_size
      print(book[l:l+page_size],"kkkkkkkkkkk")
      return book[l:l+page_size]
ob = Solution()
book = ["hello", "world", "programming", "language", "python", "c++",
"java"]
page = 0
page_size = 3
print(ob.solve(book, page, page_size))