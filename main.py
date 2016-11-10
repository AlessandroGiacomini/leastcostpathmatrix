import webapp2
import random
import string
import webbrowser
import os
import re

sample = [['46B', 'E59', 'EA', 'C1F', '45E', '63'],
          ['899', 'FFF', '926', '7AD', 'C4E', 'FFF'],
          ['E2E', '323', '6D2', '976', '83F', 'C96'],
          ['9E9', 'A8B', '9C1', '461', 'F74', 'D05'],
          ['EDD', 'E94', '5F4', 'D1D', 'D03', 'DE3'],
          ['89', '925', 'CF9', 'CA0', 'F18', '4D2']]

def generateRandom6x6HexMatrix():

  foo = [2,3]
  randomMatrix = []
  for i in range(6):
      randomMatrix.append([])
      for j in range(6):
        interval = random.choice(foo)
        randomMatrix[i].append(''.join([random.choice('0123456789ABCDEF') for x in range(interval)]))

  return randomMatrix

# Convert hex string matrix to int matrix
def getHexMatrix(matrix):

  rows = len(matrix)
  cols = len(matrix[0])

  hexMatrix = []
  for r in range(rows):
      hexMatrix.append([])
      for c in range(cols):
        hexMatrix[r].append("%4s" % int(matrix[r][c], 16))

  return hexMatrix

# Compute matrix of min costs (mincost)
def computeMinCostsMatrix(matrix):

  r = len(matrix)
  c = len(matrix[0])

  # Create mincost matrix of the same size of
  # matrix, filled by zeros
  mincost = []
  for i in range(r):
      mincost.append([])
      for j in range(c):
        mincost[i].append(0)

  # Compute mincosts on the elements of the grid
  mincost[0][0] = int(matrix[0][0], 16)

  for r in range(1, 6):
      mincost[r][0] = mincost[r-1][0] + int(matrix[r][0], 16)

  for c in range(1, 6):
      mincost[0][c] = mincost[0][c-1] + int(matrix[0][c], 16)

  for r in range(1, 6):
      for c in range(1, 6):
          mincost[r][c] = min(mincost[r-1][c], mincost[r][c-1]) + int(matrix[r][c], 16)

  return mincost


# Find the least cost path
def findMinCostsMatrixPath(mincost):

  path = ''
  r = len(mincost)-1
  c = len(mincost[0])-1
  while True:
      if r == 0 and c == 0:
          break
      if r == 0:
          c -= 1
          path += 'r,'
      elif c == 0:
          r -= 1
          path += 'd,'
      elif mincost[r-1][c] < mincost[r][c-1]:
          r -= 1
          path += 'd,'
      elif mincost[r-1][c] > mincost[r][c-1]:
          c -= 1
          path += 'r,'
  return '%s' % path[::-1][1:]

form = """
<form method="post" style="background-color: antiquewhite;">
    <h1 style="text-align: center; 
    font-style: italic; font-size: 45;">
    Find the least cost path on a Matrix
    </h1>
    <br>
    <label> 
      <ul>
      <li><h2 style="font-style: italic;">Hex Matrix:</h2></li>
      <h2>%(hexMatrix)s</h2>
      
      <li><h2 style="font-style: italic;">Int Matrix:</h2></li>
      <h2>%(intMatrix)s</h2>

      <li><h2 style="font-style: italic;">Minimun cost from left/top to right/down:</h2></li>
      <h2>%(mincost)s</h2>

      <li><h2 style="font-style: italic;">Path:</h2></li>
      <h2>%(path)s</h2>
      </ul>
    </label>
    <br>
    <div id="button1" style="text-align: center;">
      <input type="hidden" name="idp" value="general">
      <input type="submit" value="Play with a new Matrix" style="font-size: 25;">
    </div>
</form>
<form method="post" style="background-color: antiquewhite;">
    <div id="button2" style="text-align: center;">
      <input type="hidden" name="idp" value="sample">
      <input type="submit" value="Play Sample Matrix" style="font-size: 15;">
    </div>
</form> 
"""

class MainPage(webapp2.RequestHandler):

    def write_form(self, hexMatrix):    
        hexMatrix = hexMatrix
        mincostMatrix = computeMinCostsMatrix(hexMatrix)
        path = findMinCostsMatrixPath(mincostMatrix)
        intMatrix = getHexMatrix(hexMatrix)
        mincost = mincostMatrix[5][5]
        self.response.out.write(form % {"hexMatrix": hexMatrix,
                                        "intMatrix": intMatrix,
                                        "mincost": mincost,
                                        "path": path})
    def get(self):
        hexMatrix = generateRandom6x6HexMatrix()
        self.write_form(hexMatrix)

    def post(self):
        idp = self.request.get('idp')
        if idp == "general":
          hexMatrix = generateRandom6x6HexMatrix()
          self.write_form(hexMatrix)
        elif idp == "sample":
          hexMatrix = sample
          self.write_form(hexMatrix)

app = webapp2.WSGIApplication([('/', MainPage)],
                              debug=True)
