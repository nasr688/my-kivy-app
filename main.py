from kivy.app import App
from kivy.uix.button import  Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from  kivy.uix.floatlayout import  FloatLayout
from kivy.uix.image import  Image

class Myapp(App):
	def build(self):
		box=FloatLayout()
		
		#الصوره
		i=Image(source="nasr.png")
		i.size_hint=(None,None)
		i.size=(1000,2000)
		
		box.add_widget(i)
		
		#اخراج
		self.l=Label(text="welcom My Nasr")
		self.l.color=("red")
		self.l.size_hint=(None,None)
		self.lsiz=(100,100)
		self.l.pos=(400,1900)
		
		box.add_widget(self.l)
		
		#استخراج جميع الناتج عليه
		
		self.l2=Label(text="NATG")
		self.l2.color=("red")
		self.l2.size_hint=(None,None)
		self.l2.pos=(100,1700)
	
		
		box.add_widget(self.l2)
		
		
		#زر
		self.b=Button(text="Entar")
		self.b.size_hint=(None,None)
		self.b.size=(200,100)
		self.b.pos=(100,100)
		self.b.color=(1,1,0,1)
		
		box.add_widget(self.b)
		
		
		
		
		#ادخال 1
		
		self.t=TextInput(hint_text="Q1")
		self.t.size_hint=(None,None)
		self.t.size=(150,100)
		self.t.pos=(50,1100)
		
		box.add_widget(self.t)
		
		
		
		
		
		#ادخال 2
		
			
		
		self.t2=TextInput(hint_text="Q2")
		self.t2.size_hint=(None,None)
		self.t2.size=(150,100)
		self.t2.pos=(800,1100)
		
		box.add_widget(self.t2)
		
		
		#ادخال 3
		self.t3=TextInput(hint_text="volt 220")
		self.t3.size_hint=(None,None)
		self.t3.size=(200,150)
		self.t3.pos=(800,1300)
		
		box.add_widget(self.t3)
		
		#استدعاء الزر 
		
		self.b.bind(on_press=self.max)
		
		
		return box
		
		
		
		
		#الشغل
	def max(self,instince):
			try:
				self.l.text="WELCOM TO NASR MOSTFA"
				self.l.pos=(470,1900)
				
				#الحسابات
				a=float(self.t.text)
				c=float(self.t2.text)
				r=float(self.t3.text)
				
				g=a*c    #الطول فى العرض
				
				v=45/g  #عدد اللفات
				
				
				o=v*r    # عدد الفولت الواحد 
				
				oo=g*g  #الوات 
				
				gg=oo/r  #الامبير
				
				kk=oo/12
				
				self.l2.text=f"al tol al3rd   {g} \n  al volt wan     {v}\n  mgmo3 All   {o}\n  el watt  {oo} \n  AMber  {gg}  \n  amber Al Kol {kk} \n"
				self.l2.pos=(400,1600)
				
			
				
			except:
				self.l.text="ektb al acm sah"
			
			



Myapp().run()