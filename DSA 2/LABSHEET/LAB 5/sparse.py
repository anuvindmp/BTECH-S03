class SparseMatrix:
     def _init_(self, rows, cols, nzs):
          self._data = [[rows, cols, nzs]]
          self._nzs = nzs

     def _setitem_(self, key, value):
          if len(self._data)==self._nzs+1:
               print("Insertion Limit Reached: No other elements can be added")
               return
          else:
               self._data.append([key[0], key[1], value])
               header = self._data[0]
               data = sorted(self._data[1:])
               self._data = [header]
               for i in data:
                    self._data.append(i)

     def _getitem_(self, key):
          for i in self._data:
               if (i[0], i[1]) == key:
                    return i[2]
          return 0

     def _add_(self, other):
          if self._data[0][:2] == other._data[0][:2]:
               data = self._data[0]
               selfdata = set(tuple(i) for i in self._data[1:])
               otherdata = set(tuple(i) for i in other._data[1:])
               newinstance = SparseMatrix(self._data[0][0], self._data[0][1], len(selfdata.union(otherdata)))
               newinstance[tuple(data[:2])] = data[2]
               for i in sorted(selfdata.union(otherdata)):
                    newinstance[i[:2]] = i[2]
               return newinstance
          else:
               print(f"Dimension Error: the Dimensions ({self._data[0][0]}, {self._data[0][1]}) and ({other._data[0][0]}, {other._data[0][1]}) doesn't match")

     def _str_(self):
          res=""
          data = [[0]*self._data[0][1]]*self._data[0][0]
          for i in self._data[i:]:
               data[i[0]][i[1]]=i[2]
          res = str(data)
          return res