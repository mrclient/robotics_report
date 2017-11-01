#!/usr/bin/env python3
from numpy import cos, sin


class XI:
	"""XI_22"""

	def __init__(self, q=(0,0,0,0,0), dq=(0,0,0,0,0), ddq=(0,0,0,0,0), a=(0,0,0,0,0), d=(0,0,0,0,0)):
		self.q, self.dq, self.ddq = q, dq, ddq
		self.a, self.d = a, d

	def setData(self, q, dq, ddq, a, d):
		self.q, self.dq, self.ddq = q, dq, ddq
		self.a, self.d = a, d

	def opL0(self):
		"""220"""
		q, dq, ddq = self.q, self.dq, self.ddq
		a, d = self.a, self.d
		opL_0 = a[0]*(2*a[0]*sin(q[0])*cos(q[0])*dq[0]**2 + 2*a[0]*sin(q[0])*dq[0]**2 - a[0]*cos(q[0])**2*ddq[0] - 2*a[0]*cos(q[0])*ddq[0] + a[0]*ddq[2] - 2*d[0]*sin(q[0])*cos(q[0])*ddq[0] - d[0]*sin(q[0])*ddq[1] - 4*d[0]*cos(q[0])**2*dq[0]**2 - d[0]*cos(q[0])*dq[0]*dq[1] + 2*d[0]*dq[0]**2)
		return opL_0

	def opL1(self):
		"""221"""
		q, dq, ddq = self.q, self.dq, self.ddq
		a, d = self.a, self.d
		opL_1 = -a[0]*sin(q[0])**8*ddq[1] + 2*a[0]*sin(q[0])**8*ddq[2] + 2*a[0]*sin(q[0])**7*cos(q[0])*dq[0]*dq[1] + 4*a[0]*sin(q[0])**7*cos(q[0])*dq[0]*dq[2] - 2*a[0]*sin(q[0])**7*dq[0]**2 - 2*a[0]*sin(q[0])**7*dq[0]*dq[1] - a[0]*sin(q[0])**6*cos(q[0])*ddq[1] + 3*a[0]*sin(q[0])**6*ddq[1] - 4*a[0]*sin(q[0])**6*ddq[2] + 2*a[0]*sin(q[0])**5*cos(q[0])**3*dq[0]*dq[1] + 12*a[0]*sin(q[0])**5*cos(q[0])**3*dq[0]*dq[2] + 2*a[0]*sin(q[0])**5*cos(q[0])*dq[0]**2 - 2*a[0]*sin(q[0])**5*cos(q[0])*dq[0]*dq[1] - 4*a[0]*sin(q[0])**5*cos(q[0])*dq[0]*dq[2] + 6*a[0]*sin(q[0])**5*dq[0]**2 + 6*a[0]*sin(q[0])**5*dq[0]*dq[1] - a[0]*sin(q[0])**4*cos(q[0])**3*ddq[0] - 2*a[0]*sin(q[0])**4*cos(q[0])**3*ddq[1] - 3*a[0]*sin(q[0])**4*cos(q[0])*ddq[0] + a[0]*sin(q[0])**4*cos(q[0])*ddq[1] - 3*a[0]*sin(q[0])**4*ddq[1] - 2*a[0]*sin(q[0])**3*cos(q[0])**5*dq[0]*dq[1] + 12*a[0]*sin(q[0])**3*cos(q[0])**5*dq[0]*dq[2] - 8*a[0]*sin(q[0])**3*cos(q[0])**3*dq[0]*dq[2] - 6*a[0]*sin(q[0])**3*dq[0]**2 - 6*a[0]*sin(q[0])**3*dq[0]*dq[1] + a[0]*sin(q[0])**2*ddq[0] + a[0]*sin(q[0])**2*ddq[1] + 4*a[0]*sin(q[0])**2*ddq[2] - 2*a[0]*sin(q[0])*cos(q[0])**7*dq[0]*dq[1] + 4*a[0]*sin(q[0])*cos(q[0])**7*dq[0]*dq[2] - 2*a[0]*sin(q[0])*cos(q[0])**6*dq[0]**2 - 2*a[0]*sin(q[0])*cos(q[0])**6*dq[0]*dq[1] - 2*a[0]*sin(q[0])*cos(q[0])**5*dq[0]**2 + 2*a[0]*sin(q[0])*cos(q[0])**5*dq[0]*dq[1] - 4*a[0]*sin(q[0])*cos(q[0])**5*dq[0]*dq[2] + 4*a[0]*sin(q[0])*cos(q[0])**3*dq[0]**2 + 5*a[0]*sin(q[0])*dq[0]**2 + 2*a[0]*sin(q[0])*dq[0]*dq[1] + a[0]*cos(q[0])**8*ddq[1] - 2*a[0]*cos(q[0])**8*ddq[2] + a[0]*cos(q[0])**7*ddq[0] + a[0]*cos(q[0])**7*ddq[1] - a[0]*cos(q[0])**6*ddq[1] + 4*a[0]*cos(q[0])**6*ddq[2] + a[0]*cos(q[0])**5*ddq[0] - 2*a[0]*cos(q[0])**5*ddq[1] - 5*a[0]*cos(q[0])**3*ddq[0] + a[0]*cos(q[0])**3*ddq[1] - a[0]*ddq[0] - 3*d[0]*sin(q[0])**6*cos(q[0])*dq[0]*dq[1] - d[0]*sin(q[0])**5*cos(q[0])*ddq[0] - 6*d[0]*sin(q[0])**4*cos(q[0])**3*dq[0]*dq[1] + 2*d[0]*sin(q[0])**4*cos(q[0])*dq[0]*dq[1] - d[0]*sin(q[0])**3*cos(q[0])**3*ddq[0] - d[0]*sin(q[0])**3*cos(q[0])*ddq[0] + 4*d[0]*sin(q[0])**2*dq[0]**2 - 2*d[0]*sin(q[0])*cos(q[0])**3*ddq[0] - d[0]*sin(q[0])*ddq[1] + 3*d[0]*cos(q[0])**7*dq[0]*dq[1] - 5*d[0]*cos(q[0])**5*dq[0]*dq[1] + d[0]*cos(q[0])**3*dq[0]*dq[1] - 2*d[0]*dq[0]**2
		return opL_1

	def opL2(self):
		"""222"""
		q, dq, ddq = self.q, self.dq, self.ddq
		a, d = self.a, self.d
		opL_2 = -2*a[0]*sin(q[0])**7*ddq[2] + 4*a[0]*sin(q[0])**6*cos(q[0])*dq[0]*dq[2] + a[0]*sin(q[0])**6*dq[0]**2 + 6*a[0]*sin(q[0])**5*ddq[2] + 6*a[0]*sin(q[0])**4*cos(q[0])**3*dq[0]*dq[2] - 2*a[0]*sin(q[0])**4*cos(q[0])*dq[0]**2 - a[0]*sin(q[0])**4*cos(q[0])*dq[0]*dq[1] - 4*a[0]*sin(q[0])**4*cos(q[0])*dq[0]*dq[2] - 3*a[0]*sin(q[0])**4*dq[0]**2 + a[0]*sin(q[0])**3*cos(q[0])**3*ddq[0] - 6*a[0]*sin(q[0])**3*ddq[2] + 5*a[0]*sin(q[0])**2*dq[0]**2 - 2*a[0]*sin(q[0])*cos(q[0])**6*ddq[2] + a[0]*sin(q[0])*cos(q[0])**5*ddq[0] - a[0]*sin(q[0])*cos(q[0])**3*ddq[0] - a[0]*sin(q[0])*cos(q[0])*ddq[0] - a[0]*sin(q[0])*ddq[1] + 2*a[0]*sin(q[0])*ddq[2] - 2*a[0]*cos(q[0])**7*dq[0]*dq[2] + a[0]*cos(q[0])**6*dq[0]**2 + 2*a[0]*cos(q[0])**5*dq[0]**2 + a[0]*cos(q[0])**5*dq[0]*dq[1] + 4*a[0]*cos(q[0])**5*dq[0]*dq[2] - 4*a[0]*cos(q[0])**3*dq[0]**2 - 2*a[0]*cos(q[0])**3*dq[0]*dq[1] - 2*a[0]*cos(q[0])**3*dq[0]*dq[2] + 2*a[0]*cos(q[0])*dq[0]**2 - 2*a[0]*dq[0]**2 + d[0]*sin(q[0])**4*cos(q[0])*ddq[0] - d[0]*cos(q[0])**5*ddq[0] + 2*d[0]*cos(q[0])**3*ddq[0] - d[0]*cos(q[0])*ddq[0]
		return opL_2

	def opL3(self):
		"""223"""
		q, dq, ddq = self.q, self.dq, self.ddq
		a, d = self.a, self.d
		opL_3 = -2*a[0]*sin(q[0])**8*dq[0]*dq[1] + a[0]*sin(q[0])**7*ddq[1] + 2*a[0]*sin(q[0])**6*cos(q[0])*dq[0]**2 - 2*a[0]*sin(q[0])**6*cos(q[0])*dq[0]*dq[1] + 6*a[0]*sin(q[0])**6*dq[0]*dq[1] + a[0]*sin(q[0])**5*cos(q[0])**3*ddq[1] - a[0]*sin(q[0])**5*cos(q[0])*ddq[0] - 3*a[0]*sin(q[0])**5*ddq[1] - a[0]*sin(q[0])**4*cos(q[0])**3*dq[0]**2 - 3*a[0]*sin(q[0])**4*cos(q[0])**3*dq[0]*dq[1] - 5*a[0]*sin(q[0])**4*cos(q[0])*dq[0]**2 + 2*a[0]*sin(q[0])**4*cos(q[0])*dq[0]*dq[1] - 6*a[0]*sin(q[0])**4*dq[0]*dq[1] + 2*a[0]*sin(q[0])**3*cos(q[0])**5*ddq[1] - a[0]*sin(q[0])**3*cos(q[0])**3*ddq[0] - a[0]*sin(q[0])**3*cos(q[0])**3*ddq[1] + 3*a[0]*sin(q[0])**3*ddq[1] + 2*a[0]*sin(q[0])**2*dq[0]**2 + 2*a[0]*sin(q[0])**2*dq[0]*dq[1] + a[0]*sin(q[0])*cos(q[0])**7*ddq[1] + a[0]*sin(q[0])*cos(q[0])**6*ddq[1] - a[0]*sin(q[0])*cos(q[0])**5*ddq[1] - a[0]*sin(q[0])*cos(q[0])**3*ddq[0] - a[0]*sin(q[0])*ddq[0] - a[0]*sin(q[0])*ddq[1] + 2*a[0]*cos(q[0])**8*dq[0]*dq[1] + 3*a[0]*cos(q[0])**7*dq[0]**2 + a[0]*cos(q[0])**7*dq[0]*dq[1] - 2*a[0]*cos(q[0])**6*dq[0]*dq[1] - 3*a[0]*cos(q[0])**5*dq[0]**2 - 2*a[0]*cos(q[0])**5*dq[0]*dq[1] - 3*a[0]*cos(q[0])**3*dq[0]**2 + a[0]*cos(q[0])**3*dq[0]*dq[1] + 2*a[0]*cos(q[0])*dq[0]**2 - a[0]*dq[0]**2 + 2*d[0]*sin(q[0])**7*dq[0]*dq[1] + d[0]*sin(q[0])**6*cos(q[0])*ddq[1] - 4*d[0]*sin(q[0])**5*cos(q[0])*dq[0]**2 - 6*d[0]*sin(q[0])**5*dq[0]*dq[1] + 2*d[0]*sin(q[0])**4*cos(q[0])**3*ddq[1] - 4*d[0]*sin(q[0])**3*cos(q[0])**3*dq[0]**2 + 6*d[0]*sin(q[0])**3*dq[0]*dq[1] - 2*d[0]*sin(q[0])**2*ddq[0] + 2*d[0]*sin(q[0])*cos(q[0])**6*dq[0]*dq[1] - 4*d[0]*sin(q[0])*cos(q[0])**3*dq[0]**2 - 3*d[0]*sin(q[0])*dq[0]*dq[1] - d[0]*cos(q[0])**7*ddq[1] + d[0]*cos(q[0])**5*ddq[1] + d[0]*cos(q[0])**3*ddq[1] + d[0]*ddq[0]
		return opL_3

	def opL4(self):
		"""224"""
		q, dq, ddq = self.q, self.dq, self.ddq
		a, d = self.a, self.d
		opL_4 = 0
		return opL_4

	def opL5(self):
		"""225"""
		q, dq, ddq = self.q, self.dq, self.ddq
		a, d = self.a, self.d
		opL_5 = 4*sin(q[0])**7*cos(q[0])*dq[0]*dq[2] + 8*sin(q[0])**5*cos(q[0])**3*dq[0]*dq[2] - 4*sin(q[0])**5*cos(q[0])*dq[0]*dq[2] - sin(q[0])**4*cos(q[0])*ddq[0] + 4*sin(q[0])**3*cos(q[0])**5*dq[0]*dq[2] + 4*sin(q[0])*cos(q[0])**5*dq[0]*dq[2] - 4*sin(q[0])*cos(q[0])**3*dq[0]*dq[2] + sin(q[0])*dq[0]**2 + cos(q[0])**5*ddq[0] - 2*cos(q[0])**3*ddq[0] + ddq[2]
		return opL_5

	def opL6(self):
		"""226"""
		q, dq, ddq = self.q, self.dq, self.ddq
		a, d = self.a, self.d
		opL_6 = 0
		return opL_6

	def opL7(self):
		"""227"""
		q, dq, ddq = self.q, self.dq, self.ddq
		a, d = self.a, self.d
		opL_7 = 2*sin(q[0])**9*ddq[2] - 4*sin(q[0])**8*cos(q[0])*dq[0]*dq[2] - 4*sin(q[0])**7*ddq[2] - 2*sin(q[0])**6*cos(q[0])**3*dq[0]*dq[2] + 3*sin(q[0])**6*cos(q[0])*dq[0]*dq[1] + 4*sin(q[0])**6*cos(q[0])*dq[0]*dq[2] - sin(q[0])**6*dq[0]**2 + sin(q[0])**5*cos(q[0])*ddq[0] + 8*sin(q[0])**4*cos(q[0])**5*dq[0]*dq[2] + 6*sin(q[0])**4*cos(q[0])**3*dq[0]*dq[1] - 10*sin(q[0])**4*cos(q[0])**3*dq[0]*dq[2] - 2*sin(q[0])**4*cos(q[0])*dq[0]*dq[1] + 3*sin(q[0])**4*dq[0]**2 + 2*sin(q[0])**3*cos(q[0])**6*ddq[2] + 4*sin(q[0])**3*ddq[2] - 5*sin(q[0])**2*dq[0]**2 + 2*sin(q[0])*cos(q[0])**6*ddq[2] - sin(q[0])*cos(q[0])**5*ddq[0] + 2*sin(q[0])*cos(q[0])**3*ddq[0] + sin(q[0])*ddq[1] - 2*sin(q[0])*ddq[2] - 6*cos(q[0])**9*dq[0]*dq[2] - 3*cos(q[0])**7*dq[0]*dq[1] + 20*cos(q[0])**7*dq[0]*dq[2] - cos(q[0])**6*dq[0]**2 + 5*cos(q[0])**5*dq[0]*dq[1] - 22*cos(q[0])**5*dq[0]*dq[2] - cos(q[0])**3*dq[0]*dq[1] + 8*cos(q[0])**3*dq[0]*dq[2] + 2*dq[0]**2
		return opL_7

	def opL8(self):
		"""228"""
		q, dq, ddq = self.q, self.dq, self.ddq
		a, d = self.a, self.d
		opL_8 = 0
		return opL_8

	def opL9(self):
		"""229"""
		q, dq, ddq = self.q, self.dq, self.ddq
		a, d = self.a, self.d
		opL_9 = 8*sin(q[0])**9*dq[0]*dq[2] + 2*sin(q[0])**8*cos(q[0])*ddq[2] - 2*sin(q[0])**7*dq[0]*dq[1] - 20*sin(q[0])**7*dq[0]*dq[2] + 4*sin(q[0])**6*cos(q[0])**3*ddq[2] - sin(q[0])**6*cos(q[0])*ddq[1] - 2*sin(q[0])**6*cos(q[0])*ddq[2] + 6*sin(q[0])**5*cos(q[0])*dq[0]**2 + 6*sin(q[0])**5*dq[0]*dq[1] + 12*sin(q[0])**5*dq[0]*dq[2] + 2*sin(q[0])**4*cos(q[0])**5*ddq[2] - 2*sin(q[0])**4*cos(q[0])**3*ddq[1] + 8*sin(q[0])**3*cos(q[0])**6*dq[0]*dq[2] + 4*sin(q[0])**3*cos(q[0])**3*dq[0]**2 - 4*sin(q[0])**3*cos(q[0])*dq[0]**2 - 6*sin(q[0])**3*dq[0]*dq[1] + 4*sin(q[0])**3*dq[0]*dq[2] + sin(q[0])**2*ddq[0] - 2*sin(q[0])*cos(q[0])**6*dq[0]*dq[1] + 4*sin(q[0])*cos(q[0])**6*dq[0]*dq[2] - 2*sin(q[0])*cos(q[0])**5*dq[0]**2 + 4*sin(q[0])*cos(q[0])**3*dq[0]**2 + 3*sin(q[0])*dq[0]*dq[1] - 4*sin(q[0])*dq[0]*dq[2] + cos(q[0])**7*ddq[1] - 2*cos(q[0])**7*ddq[2] - cos(q[0])**5*ddq[1] + 4*cos(q[0])**5*ddq[2] - cos(q[0])**3*ddq[1] - 2*cos(q[0])**3*ddq[2]
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

