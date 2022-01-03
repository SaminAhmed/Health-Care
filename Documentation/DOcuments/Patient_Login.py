

def homepage(request):
	""""
    This function is used to show up a home page of the website.

    :parameter request: it is an HttpResponse from user

    Any user can view this home page of the website.

    :return: HttpResponse which is a HTML page.

    :return type: HttpResponse
    """


def loginpage(request):
    """
    This function is used for loging in as a patient.

    :parameter request: it is an HttpResponse from user

    Users who have registered to this website can login through this page.

    :variable type: string

    :return: HttpResponse of patient home page which will redirect to a HTML page

    :return type: HttpResponse
    """

def Logout(request):
    """
    This function is used for loging out as a user.

    :parameter request: it is an HttpResponse from user

    Users who have logged in to this website can log out through this page.

    :return: HttpResponse of HTML file which is a login page

    :return type: HttpResponse
    """

	