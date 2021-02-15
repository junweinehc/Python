{\rtf1\ansi\ansicpg1252\cocoartf2513
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 %matplotlib inline\
import pandas as pd\
import numpy as np\
import seaborn as sns\
import matplotlib.pyplot as plt\
\
a = np.array([[11, 12, 13, 14, 15],\
              [16, 17, 18, 19, 20],\
              [21, 22, 23, 24, 25],\
              [26, 27, 28 ,29, 30],\
              [31, 32, 33, 34, 35]])\
\
print(type(a)) # >>><class 'numpy.ndarray'>\
print(a.dtype) # >>>int64\
print(a.size) # >>>25\
print(a.shape) # >>>(5, 5)\
print(a.itemsize) # >>>8\
print(a.ndim) # >>>2\
print(a.nbytes) # >>>200\
\
a = np.arange(25)\
a = a.reshape(5,5)\
a\
\
b = np.array([10, 62, 1, 14, 2, 56, 79, 2, 1, 45,\
              4, 92, 5, 55, 63, 43, 35, 6, 53, 24,\
              56, 3, 56, 44, 78])\
b = b.reshape((5,5))\
b\
\
print(a + b)\
print(a - b)\
print(a * b)\
print(a / b)\
print(a ** 2)\
print(a < b) \
print(a > b)\
\
print(a.dot(b))\
\
a = np.arange(10)\
\
print(a.sum()) # >>>45\
print(a.min()) # >>>0\
print(a.max()) # >>>9\
print(a.cumsum())}