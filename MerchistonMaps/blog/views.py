from django.shortcuts import render

posts = [
	{

		'author': 'Euan',
		'title': 'Blog Post 1',
		'content': 'WOOOOOOOOOOOOOOOOOOOOOOOOOOOO',
		'date_posted': 'July 17, 2021'
	},
	{

		'author': 'Pusheen',
		'title': 'Blog Post 2',
		'content': 'Second post content',
		'date_posted': 'July 18, 2021',
	}
]

def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'blog/bloghome.html', context)


def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})
