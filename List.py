{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f15c3c09",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Cherry\n",
      "Banana\n"
     ]
    }
   ],
   "source": [
    "#LIst\n",
    "a=[\"Apple\",\"Banana\",\"Cherry\"]\n",
    "print(a[2])\n",
    "print(a[-2])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ed292c5e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['a', 'e', 'c', 'd']\n"
     ]
    }
   ],
   "source": [
    "#Insert and Remove\n",
    "\n",
    "a=[\"a\",\"b\",\"c\",\"d\"]\n",
    "a.insert(2,\"e\")\n",
    "a.remove(\"b\")\n",
    "print(a)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "2481b3d3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['a', 'b']\n"
     ]
    }
   ],
   "source": [
    "#POP\n",
    "a=[\"a\",\"b\",\"c\",\"d\"]\n",
    "a.pop()\n",
    "a.pop(2)\n",
    "\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "38e70520",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['a', 'b', 'c', 'd']\n"
     ]
    }
   ],
   "source": [
    "#Sort\n",
    "a=[\"a\",\"b\",\"c\",\"d\"]\n",
    "a.sort(reverse=True)\n",
    "a.reverse()\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "695489a0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 4, 6, 8, 10]\n"
     ]
    }
   ],
   "source": [
    "#List Comprehesion\n",
    "\n",
    "a=[x*2 for x in range(1,6)]\n",
    "print(a)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "3ca4d05b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['a', 'b', 'c', 'd', 'e', 'f', 'h']\n"
     ]
    }
   ],
   "source": [
    "a=[\"a\",\"b\",\"c\",\"d\"]\n",
    "a.extend([\"e\",\"f\",\"h\"])\n",
    "print(a)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "378f8c45",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['a', 'b', 'c', 'd']\n"
     ]
    }
   ],
   "source": [
    "#Copy\n",
    "a=[\"a\",\"b\",\"c\",\"d\"]\n",
    "b=a.copy()\n",
    "print(b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "a01d4b39",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[]\n"
     ]
    }
   ],
   "source": [
    "#Clear\n",
    "a=[\"a\",\"b\",\"c\",\"d\"]\n",
    "a.clear()\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "6fc84196",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "#Membership Opeartor\n",
    "a=[\"a\",\"b\",\"c\",\"d\"]\n",
    "print(\"e\" in a)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "33fbfda3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['a', 'h', 'c', 'd']\n"
     ]
    }
   ],
   "source": [
    "#Updating List\n",
    "a=[\"a\",\"b\",\"c\",\"d\"]\n",
    "a[1]=\"h\"\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "d6ab729b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['a', 'b', 'd']\n"
     ]
    }
   ],
   "source": [
    "#Deleting a List\n",
    "a=[\"a\",\"b\",\"c\",\"d\"]\n",
    "del a[2]\n",
    "print(a)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b8d1cbaf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "c\n",
      "d\n",
      "('b', 'a')\n",
      "('a', 'b', 'c', 'd')\n",
      "3\n",
      "0\n"
     ]
    }
   ],
   "source": [
    "#Tuple\n",
    "a=(\"a\",\"b\",\"c\",\"d\",\"a\",\"a\")\n",
    "#indexing\n",
    "print (a[2])\n",
    "#Negative Indexing\n",
    "print(a[-3])\n",
    "#Slicing\n",
    "print(a[1::3])\n",
    "print(a[:4])\n",
    "#Count\n",
    "print(a.count(\"a\"))\n",
    "#Index\n",
    "print(a.index(\"a\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "7f3fa59e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('Mohan', 31, 'Python')\n"
     ]
    }
   ],
   "source": [
    "#Packing\n",
    "'''a=(\"Mohan\",31,\"Python\")\n",
    "print(a)'''\n",
    "#Unpacking\n",
    "b=(\"Mohan\",31,\"Python\")\n",
    "name,age,course=b\n",
    "print(b)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "f6345892",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "3\n",
      "('Mohan', 31, 'Python')\n"
     ]
    }
   ],
   "source": [
    "#Membership Opeartor\n",
    "a=(\"Mohan\",31,\"Python\")\n",
    "print(31 in a)\n",
    "print(len(a))\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "ab4ec090",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(('Mohan', 'raj'), ('Python', 'Java'))\n",
      "('Mohan', 'raj')\n",
      "(('Mohan', 'raj'), ('Python', 'Java'), 'C++')\n"
     ]
    }
   ],
   "source": [
    "#Nested Tuple\n",
    "a=((\"Mohan\",\"raj\"),(\"Python\",\"Java\"))\n",
    "print(a)\n",
    "print(a[0])\n",
    "#Conversting tuple to list\n",
    "a=list(a)\n",
    "a.append(\"C++\")\n",
    "a=tuple(a)\n",
    "print(a)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.14.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
