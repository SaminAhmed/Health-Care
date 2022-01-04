

def homepage(request):
	return render(request,'index.html')

	"""
		The view will render the homepage.

		:Parameter: request

		Admin can view this homepage of this website

		:Return: renders the homepage

	"""


def Login_admin(request):

	"""
		 This is the login admin page.

		 :Parameter: request

		 When admin put his username and password then he/she can login to the admin dashboard

		 :Return: renders the login admin page

	"""
	
def AdminHome(request):

	"""
		This is the admin dashboard

		:Parameter: request

		From the dashboard he will notify his work.After login,admin can view the dashboard

		:Return: renders the login home page

	"""

def Logout_admin(request):


  """
       From this admin can logout from the system

       :Parameter: request

       Whenever admin login to the system,admin can also back to homepage

       :Return: redirect to the login_admin


  """