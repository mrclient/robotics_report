#!/usr/bin/env python3
from numpy import cos, sin


class XI:
	"""XI_21"""

	def __init__(self, q=(0,0,0,0,0), dq=(0,0,0,0,0), ddq=(0,0,0,0,0), a=(0,0,0,0,0), d=(0,0,0,0,0)):
		self.q, self.dq, self.ddq = q, dq, ddq
		self.a, self.d = a, d

	def setData(self, q, dq, ddq, a, d):
		self.q, self.dq, self.ddq = q, dq, ddq
		self.a, self.d = a, d

	def opL0(self):
		"""210"""
		q, dq, ddq = self.q, self.dq, self.ddq
		a, d = self.a, self.d
		opL_0 = -2*a[0]**2*sin(q[0])**3*cos(q[0])*dq[0]*dq[1] + 3*a[0]**2*sin(q[0])**3*dq[0]**2 - a[0]**2*sin(q[0])**2*ddq[0] - a[0]**2*sin(q[0])**2*ddq[1] - 2*a[0]**2*sin(q[0])*cos(q[0])**3*dq[0]*dq[1] - 2*a[0]**2*sin(q[0])*cos(q[0])*dq[0]**2 - 2*a[0]**2*sin(q[0])*dq[0]**2 - 2*a[0]**2*sin(q[0])*dq[0]*dq[1] + a[0]**2*cos(q[0])**3*ddq[0] - a[0]**2*cos(q[0])*ddq[0] + 2*a[0]**2*cos(q[0])*ddq[1] + 2*a[0]**2*ddq[1] - a[0]*d[0]*sin(q[0])**4*cos(q[0])*dq[0]*dq[2] + a[0]*d[0]*sin(q[0])**3*cos(q[0])*ddq[0] + a[0]*d[0]*sin(q[0])*cos(q[0])**3*ddq[0] - a[0]*d[0]*sin(q[0])*cos(q[0])*ddq[0] - a[0]*d[0]*sin(q[0])*ddq[0] - a[0]*d[0]*sin(q[0])*ddq[2] + a[0]*d[0]*cos(q[0])**5*dq[0]*dq[2] - 2*a[0]*d[0]*cos(q[0])**3*dq[0]*dq[2] - a[0]*d[0]*cos(q[0])*dq[0]**2 - d[0]**2*sin(q[0])*dq[0]**2 + d[0]**2*cos(q[0])*ddq[0] + d[0]**2*ddq[1]
		return opL_0

	def opL1(self):
		"""211"""
		q, dq, ddq = self.q, self.dq, self.ddq
		a, d = self.a, self.d
		opL_1 = 2*a[0]*sin(q[0])**5*cos(q[0])*dq[0]*dq[2] - a[0]*sin(q[0])**4*cos(q[0])*ddq[2] - 4*a[0]*sin(q[0])**3*cos(q[0])*dq[0]*dq[1] - 2*a[0]*sin(q[0])**3*cos(q[0])*dq[0]*dq[2] + 6*a[0]*sin(q[0])**3*dq[0]**2 - a[0]*sin(q[0])**2*ddq[0] - 2*a[0]*sin(q[0])**2*ddq[1] - 2*a[0]*sin(q[0])*cos(q[0])**5*dq[0]*dq[2] - 4*a[0]*sin(q[0])*cos(q[0])**3*dq[0]*dq[1] + 2*a[0]*sin(q[0])*cos(q[0])**3*dq[0]*dq[2] - 2*a[0]*sin(q[0])*cos(q[0])*dq[0]**2 - 4*a[0]*sin(q[0])*dq[0]**2 - 2*a[0]*sin(q[0])*dq[0]*dq[1] + a[0]*cos(q[0])**5*ddq[2] + 2*a[0]*cos(q[0])**3*ddq[0] - 2*a[0]*cos(q[0])**3*ddq[2] - 2*a[0]*cos(q[0])*ddq[0] + 2*a[0]*cos(q[0])*ddq[1] + a[0]*cos(q[0])*ddq[2] + 2*a[0]*ddq[1] - 3*d[0]*sin(q[0])**4*cos(q[0])*dq[0]*dq[2] - d[0]*sin(q[0])*ddq[2] + 3*d[0]*cos(q[0])**5*dq[0]*dq[2] - 6*d[0]*cos(q[0])**3*dq[0]*dq[2] + 2*d[0]*cos(q[0])*dq[0]*dq[2]
		return opL_1

	def opL2(self):
		"""212"""
		q, dq, ddq = self.q, self.dq, self.ddq
		a, d = self.a, self.d
		opL_2 = -2*a[0]*sin(q[0])**2*dq[0]**2 + a[0]*sin(q[0])*cos(q[0])*ddq[0] - a[0]*sin(q[0])*ddq[2] - a[0]*cos(q[0])*dq[0]*dq[2] + a[0]*dq[0]**2 - d[0]*sin(q[0])*dq[0]**2 + d[0]*cos(q[0])*ddq[0] + 2*d[0]*ddq[1]
		return opL_2

	def opL3(self):
		"""213"""
		q, dq, ddq = self.q, self.dq, self.ddq
		a, d = self.a, self.d
		opL_3 = a[0]*sin(q[0])**6*dq[0]*dq[2] - 2*a[0]*sin(q[0])**4*cos(q[0])*dq[0]*dq[2] - 3*a[0]*sin(q[0])**4*dq[0]*dq[2] + a[0]*sin(q[0])**3*cos(q[0])**3*ddq[2] + 2*a[0]*sin(q[0])**3*cos(q[0])*ddq[1] - 2*a[0]*sin(q[0])**3*ddq[0] - 2*a[0]*sin(q[0])**2*dq[0]**2 - 4*a[0]*sin(q[0])**2*dq[0]*dq[1] + 3*a[0]*sin(q[0])**2*dq[0]*dq[2] + a[0]*sin(q[0])*cos(q[0])**5*ddq[2] + 2*a[0]*sin(q[0])*cos(q[0])**3*ddq[1] - a[0]*sin(q[0])*cos(q[0])**3*ddq[2] + a[0]*sin(q[0])*cos(q[0])*ddq[0] + a[0]*sin(q[0])*ddq[0] + 2*a[0]*sin(q[0])*ddq[1] + a[0]*cos(q[0])**6*dq[0]*dq[2] + 2*a[0]*cos(q[0])**5*dq[0]*dq[2] + 6*a[0]*cos(q[0])**3*dq[0]**2 - 4*a[0]*cos(q[0])**3*dq[0]*dq[2] - 5*a[0]*cos(q[0])*dq[0]**2 + 2*a[0]*cos(q[0])*dq[0]*dq[1] + 2*a[0]*cos(q[0])*dq[0]*dq[2] + a[0]*dq[0]**2 + 2*a[0]*dq[0]*dq[1] - a[0]*dq[0]*dq[2] + d[0]*sin(q[0])**4*cos(q[0])*ddq[2] - d[0]*sin(q[0])*dq[0]*dq[2] - d[0]*cos(q[0])**5*ddq[2] + 2*d[0]*cos(q[0])**3*ddq[2] - d[0]*ddq[0]
		return opL_3

	def opL4(self):
		"""214"""
		q, dq, ddq = self.q, self.dq, self.ddq
		a, d = self.a, self.d
		opL_4 = (-sin(q[0])*dq[0]**2 + 4*sin(2*q[0])*cos(2*q[0])*dq[0]*dq[2] + 4*sin(2*q[0])*dq[0]*dq[1] + 3*sin(3*q[0])*dq[0]**2 - 2*sin(4*q[0])*dq[0]*dq[2] + cos(q[0])*ddq[0] - 2*cos(2*q[0])*ddq[1] - cos(3*q[0])*ddq[0] + 2*ddq[1])/4
		return opL_4

	def opL5(self):
		"""215"""
		q, dq, ddq = self.q, self.dq, self.ddq
		a, d = self.a, self.d
		opL_5 = 0
		return opL_5

	def opL6(self):
		"""216"""
		q, dq, ddq = self.q, self.dq, self.ddq
		a, d = self.a, self.d
		opL_6 = 2*sin(q[0])**5*cos(q[0])*dq[0]*dq[2] - 2*sin(q[0])**3*cos(q[0])*dq[0]*dq[1] - 2*sin(q[0])**3*cos(q[0])*dq[0]*dq[2] + 3*sin(q[0])**3*dq[0]**2 - 2*sin(q[0])*cos(q[0])**5*dq[0]*dq[2] - 2*sin(q[0])*cos(q[0])**3*dq[0]*dq[1] + 2*sin(q[0])*cos(q[0])**3*dq[0]*dq[2] - 2*sin(q[0])*dq[0]**2 + cos(q[0])**3*ddq[0] + cos(q[0])**2*ddq[1] - cos(q[0])*ddq[0]
		return opL_6

	def opL7(self):
		"""217"""
		q, dq, ddq = self.q, self.dq, self.ddq
		a, d = self.a, self.d
		opL_7 = 3*sin(q[0])**4*cos(q[0])*dq[0]*dq[2] + 2*sin(q[0])**2*dq[0]**2 - sin(q[0])*cos(q[0])*ddq[0] + sin(q[0])*ddq[2] - 3*cos(q[0])**5*dq[0]*dq[2] + 6*cos(q[0])**3*dq[0]*dq[2] - 2*cos(q[0])*dq[0]*dq[2] - dq[0]**2
		return opL_7

	def opL8(self):
		"""218"""
		q, dq, ddq = self.q, self.dq, self.ddq
		a, d = self.a, self.d
		opL_8 = -sin(q[0])**6*dq[0]*dq[2] + sin(q[0])**5*cos(q[0])*ddq[2] + 3*sin(q[0])**4*dq[0]*dq[2] - 2*sin(q[0])**3*cos(q[0])*ddq[1] - sin(q[0])**3*cos(q[0])*ddq[2] + 2*sin(q[0])**3*ddq[0] + 4*sin(q[0])**2*dq[0]*dq[1] - 3*sin(q[0])**2*dq[0]*dq[2] - sin(q[0])*cos(q[0])**5*ddq[2] - 2*sin(q[0])*cos(q[0])**3*ddq[1] + sin(q[0])*cos(q[0])**3*ddq[2] - sin(q[0])*ddq[0] - cos(q[0])**6*dq[0]*dq[2] - 6*cos(q[0])**3*dq[0]**2 + 5*cos(q[0])*dq[0]**2 - 2*dq[0]*dq[1] + dq[0]*dq[2]
		return opL_8

	def opL9(self):
		"""219"""
		q, dq, ddq = self.q, self.dq, self.ddq
		a, d = self.a, self.d
		opL_9 = -2*sin(q[0])**7*dq[0]*dq[2] - sin(q[0])**6*cos(q[0])*ddq[2] + 6*sin(q[0])**5*dq[0]*dq[2] - 2*sin(q[0])**3*cos(q[0])*dq[0]**2 - 6*sin(q[0])**3*dq[0]*dq[2] - 2*sin(q[0])*cos(q[0])**6*dq[0]*dq[2] - 2*sin(q[0])*cos(q[0])**3*dq[0]**2 + 3*sin(q[0])*dq[0]*dq[2] - cos(q[0])**7*ddq[2] + 3*cos(q[0])**5*ddq[2] - 3*cos(q[0])**3*ddq[2] + cos(q[0])**2*ddq[0]
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

