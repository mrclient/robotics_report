#!/usr/bin/env python3
from numpy import cos, sin


class XI:
	"""XI_00"""

	def __init__(self, q=(0,0,0,0,0), dq=(0,0,0,0,0), ddq=(0,0,0,0,0), a=(0,0,0,0,0), d=(0,0,0,0,0)):
		self.q, self.dq, self.ddq = q, dq, ddq
		self.a, self.d = a, d

	def setData(self, q, dq, ddq, a, d):
		self.q, self.dq, self.ddq = q, dq, ddq
		self.a, self.d = a, d

	def opL0(self):
		"""000"""
		q, dq, ddq = self.q, self.dq, self.ddq
		a, d = self.a, self.d
		opL_0 = (-a[0]*sin(q[0])**2 - a[0]*cos(q[0])**2)*(-a[0]*sin(q[0])**2*ddq[0]/2 - a[0]*cos(q[0])**2*ddq[0]/2) + (-a[0]*sin(q[0])**2/2 - a[0]*cos(q[0])**2/2)*(-a[0]*sin(q[0])**2*ddq[0] - a[0]*cos(q[0])**2*ddq[0])
		return opL_0

	def opL1(self):
		"""001"""
		q, dq, ddq = self.q, self.dq, self.ddq
		a, d = self.a, self.d
		opL_1 = a[0]*sin(q[0])**2*ddq[0] + a[0]*cos(q[0])**2*ddq[0] - (-a[0]*sin(q[0])**2 - a[0]*cos(q[0])**2)*ddq[0]
		return opL_1

	def opL2(self):
		"""002"""
		q, dq, ddq = self.q, self.dq, self.ddq
		a, d = self.a, self.d
		opL_2 = 0
		return opL_2

	def opL3(self):
		"""003"""
		q, dq, ddq = self.q, self.dq, self.ddq
		a, d = self.a, self.d
		opL_3 = 0
		return opL_3

	def opL4(self):
		"""004"""
		q, dq, ddq = self.q, self.dq, self.ddq
		a, d = self.a, self.d
		opL_4 = 0
		return opL_4

	def opL5(self):
		"""005"""
		q, dq, ddq = self.q, self.dq, self.ddq
		a, d = self.a, self.d
		opL_5 = ddq[0]
		return opL_5

	def opL6(self):
		"""006"""
		q, dq, ddq = self.q, self.dq, self.ddq
		a, d = self.a, self.d
		opL_6 = 0
		return opL_6

	def opL7(self):
		"""007"""
		q, dq, ddq = self.q, self.dq, self.ddq
		a, d = self.a, self.d
		opL_7 = 0
		return opL_7

	def opL8(self):
		"""008"""
		q, dq, ddq = self.q, self.dq, self.ddq
		a, d = self.a, self.d
		opL_8 = 0
		return opL_8

	def opL9(self):
		"""009"""
		q, dq, ddq = self.q, self.dq, self.ddq
		a, d = self.a, self.d
		opL_9 = 0
		return opL_9

	def getXI(self, q, dq, ddq, a, d):
		self.setData(q, dq, ddq, a, d)
		XI = [0 for i in range(10)]
		XI[0] = self.opL0()
		XI[1] = self.opL1()
		XI[2] = self.opL2()
		XI[3] = self.opL3()
		XI[4] = self.opL4()
		XI[5] = self.opL5()
		XI[6] = self.opL6()
		XI[7] = self.opL7()
		XI[8] = self.opL8()
		XI[9] = self.opL9()
		return XI

