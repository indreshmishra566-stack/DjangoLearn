from django.db import migrations


CHAPTERS = [
    {"order": 1,  "slug": "intro",       "icon": "🐍", "title": "What is Django?",          "color": "#44b78b"},
    {"order": 3,  "slug": "setup",       "icon": "🛠️", "title": "Setup & Installation",      "color": "#e74c3c"},
    {"order": 5,  "slug": "settings",    "icon": "⚙️",  "title": "Settings & Config",         "color": "#9b59b6"},
    {"order": 11, "slug": "models",      "icon": "🗄️", "title": "Models & Database",          "color": "#3498db"},
    {"order": 8,  "slug": "views",       "icon": "👁️", "title": "Views",                      "color": "#e67e22"},
    {"order": 7,  "slug": "urls",        "icon": "🔗", "title": "URL Routing",                "color": "#1abc9c"},
    {"order": 10, "slug": "templates",   "icon": "🎨", "title": "Templates",                  "color": "#f39c12"},
    {"order": 14, "slug": "forms",       "icon": "📋", "title": "Forms",                      "color": "#e91e63"},
    {"order": 15, "slug": "admin",       "icon": "🔧", "title": "Django Admin",               "color": "#16a085"},
    {"order": 17, "slug": "auth",        "icon": "🔐", "title": "Authentication",             "color": "#c0392b"},
    {"order": 21, "slug": "staticmedia", "icon": "📁", "title": "Static & Media Files",       "color": "#7f8c8d"},
    {"order": 31, "slug": "drf",         "icon": "🚀", "title": "Django REST Framework",      "color": "#2980b9"},
]

SECTIONS = [
    # ── INTRO ──────────────────────────────────────────────────────────────────
    {"chapter_slug": "intro", "order": 1, "section_type": "theory", "heading": "Introduction to Django",
     "content": (
         "Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. "
         "Built in 2003 and released in 2005, it follows the MVT (Model-View-Template) pattern.\n\n"
         "Django's motto: 'The web framework for perfectionists with deadlines.'\n\n"
         "Key Features:\n"
         "• Built-in admin interface\n"
         "• ORM — interact with DB using Python\n"
         "• URL routing and template engine\n"
         "• Built-in authentication system\n"
         "• Security: CSRF, XSS, SQL injection protection\n"
         "• Used by Instagram, Pinterest, NASA"
     ), "code": ""},

    {"chapter_slug": "intro", "order": 2, "section_type": "theory", "heading": "MVT Architecture",
     "content": (
         "Django uses MVT — Model, View, Template:\n\n"
         "• Model — Defines your data structure. Maps Python classes to database tables.\n"
         "• View — Business logic. Receives HTTP requests, talks to the model, returns responses.\n"
         "• Template — Presentation layer. HTML with Django Template Language for dynamic content.\n"
         "• URL Dispatcher — Routes incoming URLs to the correct view.\n\n"
         "Flow: User Request → URL Dispatcher → View → Model → Template → Response"
     ), "code": ""},

    # ── SETUP ──────────────────────────────────────────────────────────────────
    {"chapter_slug": "setup", "order": 1, "section_type": "theory", "heading": "Prerequisites",
     "content": (
         "Before installing Django, you need:\n\n"
         "• Python 3.8+ — download from python.org\n"
         "• pip — comes with Python 3.4+\n"
         "• Virtual Environment — strongly recommended\n\n"
         "Why virtual environments? Each project may need different package versions. "
         "A venv keeps dependencies isolated so projects don't conflict."
     ), "code": ""},

    {"chapter_slug": "setup", "order": 2, "section_type": "commands", "heading": "Installation Commands",
     "content": "", "code": ""},

    {"chapter_slug": "setup", "order": 3, "section_type": "code", "heading": "Project Structure",
     "content": "", "code": (
         "mysite/\n"
         "├── manage.py            # CLI tool for project management\n"
         "├── mysite/              # Project config package\n"
         "│   ├── settings.py      # All project settings\n"
         "│   ├── urls.py          # Root URL configuration\n"
         "│   └── wsgi.py          # WSGI entry point\n"
         "└── blog/                # An app you created\n"
         "    ├── admin.py         # Register models with admin\n"
         "    ├── models.py        # Database models\n"
         "    ├── views.py         # View functions/classes\n"
         "    ├── urls.py          # App-level URL routes\n"
         "    └── migrations/      # Auto-generated DB migrations"
     )},

    # ── SETTINGS ───────────────────────────────────────────────────────────────
    {"chapter_slug": "settings", "order": 1, "section_type": "theory", "heading": "Understanding settings.py",
     "content": (
         "The settings.py file is the control center of your Django project.\n\n"
         "Key Settings:\n"
         "• DEBUG — True in development, always False in production\n"
         "• ALLOWED_HOSTS — Valid hostnames for your site\n"
         "• INSTALLED_APPS — All apps Django should load\n"
         "• DATABASES — Database connection config\n"
         "• STATIC_URL — URL prefix for static files\n"
         "• MEDIA_URL / MEDIA_ROOT — For user-uploaded files\n"
         "• SECRET_KEY — Used for cryptographic signing — keep it secret!"
     ), "code": ""},

    {"chapter_slug": "settings", "order": 2, "section_type": "code", "heading": "Important settings.py Sections",
     "content": "", "code": (
         "SECRET_KEY = 'your-secret-key-here'\n"
         "DEBUG = True\n"
         "ALLOWED_HOSTS = ['localhost', '127.0.0.1']\n\n"
         "INSTALLED_APPS = [\n"
         "    'django.contrib.admin',\n"
         "    'django.contrib.auth',\n"
         "    'django.contrib.contenttypes',\n"
         "    'django.contrib.sessions',\n"
         "    'django.contrib.messages',\n"
         "    'django.contrib.staticfiles',\n"
         "    'blog',           # Your custom app\n"
         "]\n\n"
         "DATABASES = {\n"
         "    'default': {\n"
         "        'ENGINE': 'django.db.backends.sqlite3',\n"
         "        'NAME': BASE_DIR / 'db.sqlite3',\n"
         "    }\n"
         "}\n\n"
         "STATIC_URL = '/static/'\n"
         "MEDIA_URL = '/media/'\n"
         "MEDIA_ROOT = BASE_DIR / 'media'"
     )},

    # ── MODELS ─────────────────────────────────────────────────────────────────
    {"chapter_slug": "models", "order": 1, "section_type": "theory", "heading": "Django ORM & Models",
     "content": (
         "A Model is a Python class that maps to a database table. Django's ORM lets you work "
         "with your database using Python instead of raw SQL.\n\n"
         "Common Field Types:\n"
         "• CharField — short text (max_length required)\n"
         "• TextField — long text\n"
         "• IntegerField — whole numbers\n"
         "• BooleanField — True/False\n"
         "• DateTimeField — date and time\n"
         "• EmailField — validated email\n"
         "• ImageField / FileField — file uploads\n"
         "• ForeignKey — many-to-one relationship\n"
         "• ManyToManyField — many-to-many\n"
         "• OneToOneField — one-to-one"
     ), "code": ""},

    {"chapter_slug": "models", "order": 2, "section_type": "code", "heading": "Defining Models",
     "content": "", "code": (
         "# blog/models.py\n"
         "from django.db import models\n"
         "from django.contrib.auth.models import User\n\n"
         "class Category(models.Model):\n"
         "    name = models.CharField(max_length=100)\n"
         "    slug = models.SlugField(unique=True)\n\n"
         "    def __str__(self):\n"
         "        return self.name\n\n"
         "    class Meta:\n"
         "        ordering = ['name']\n\n\n"
         "class Post(models.Model):\n"
         "    STATUS_CHOICES = [\n"
         "        ('draft', 'Draft'),\n"
         "        ('published', 'Published'),\n"
         "    ]\n"
         "    title      = models.CharField(max_length=200)\n"
         "    slug       = models.SlugField(unique=True)\n"
         "    author     = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')\n"
         "    category   = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)\n"
         "    body       = models.TextField()\n"
         "    status     = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')\n"
         "    created_at = models.DateTimeField(auto_now_add=True)\n"
         "    updated_at = models.DateTimeField(auto_now=True)\n\n"
         "    def __str__(self):\n"
         "        return self.title\n\n"
         "    class Meta:\n"
         "        ordering = ['-created_at']"
     )},

    {"chapter_slug": "models", "order": 3, "section_type": "commands", "heading": "Migration Commands",
     "content": "", "code": ""},

    {"chapter_slug": "models", "order": 4, "section_type": "code", "heading": "Django ORM Queries",
     "content": "", "code": (
         "# python manage.py shell\n"
         "from blog.models import Post\n\n"
         "# CREATE\n"
         "post = Post.objects.create(title='Hello', slug='hello', body='...')\n\n"
         "# READ all\n"
         "posts = Post.objects.all()\n\n"
         "# FILTER\n"
         "published = Post.objects.filter(status='published')\n\n"
         "# GET single\n"
         "post = Post.objects.get(id=1)\n\n"
         "# ORDER BY\n"
         "latest = Post.objects.order_by('-created_at')\n\n"
         "# LIMIT\n"
         "top5 = Post.objects.all()[:5]\n\n"
         "# UPDATE\n"
         "Post.objects.filter(id=1).update(status='published')\n\n"
         "# DELETE\n"
         "Post.objects.filter(status='draft').delete()\n\n"
         "# COUNT\n"
         "total = Post.objects.count()\n\n"
         "# SEARCH\n"
         "results = Post.objects.filter(title__icontains='django')"
     )},

    # ── VIEWS ──────────────────────────────────────────────────────────────────
    {"chapter_slug": "views", "order": 1, "section_type": "theory", "heading": "Function-Based vs Class-Based Views",
     "content": (
         "Views receive HTTP requests and return HTTP responses.\n\n"
         "Function-Based Views (FBV) — Simple Python functions. Explicit, easy to read.\n\n"
         "Class-Based Views (CBV) — Python classes. More reusable, less code for CRUD.\n\n"
         "Built-in Generic CBVs:\n"
         "• ListView — display a list of objects\n"
         "• DetailView — display a single object\n"
         "• CreateView — form to create an object\n"
         "• UpdateView — form to update an object\n"
         "• DeleteView — confirm and delete\n"
         "• TemplateView — render a template"
     ), "code": ""},

    {"chapter_slug": "views", "order": 2, "section_type": "code", "heading": "Function-Based Views",
     "content": "", "code": (
         "# blog/views.py\n"
         "from django.shortcuts import render, get_object_or_404, redirect\n"
         "from django.http import HttpResponse, JsonResponse\n"
         "from .models import Post\n\n"
         "def home(request):\n"
         "    return HttpResponse('<h1>Hello Django!</h1>')\n\n"
         "def post_list(request):\n"
         "    posts = Post.objects.filter(status='published')\n"
         "    return render(request, 'blog/post_list.html', {'posts': posts})\n\n"
         "def post_detail(request, slug):\n"
         "    post = get_object_or_404(Post, slug=slug, status='published')\n"
         "    return render(request, 'blog/post_detail.html', {'post': post})\n\n"
         "def create_post(request):\n"
         "    if request.method == 'POST':\n"
         "        title = request.POST.get('title')\n"
         "        body  = request.POST.get('body')\n"
         "        Post.objects.create(title=title, body=body)\n"
         "        return redirect('post_list')\n"
         "    return render(request, 'blog/create_post.html')\n\n"
         "def api_posts(request):\n"
         "    posts = list(Post.objects.values('id', 'title', 'status'))\n"
         "    return JsonResponse({'posts': posts})"
     )},

    {"chapter_slug": "views", "order": 3, "section_type": "code", "heading": "Class-Based Views",
     "content": "", "code": (
         "from django.views.generic import (\n"
         "    ListView, DetailView, CreateView, UpdateView, DeleteView\n"
         ")\n"
         "from django.urls import reverse_lazy\n"
         "from .models import Post\n\n"
         "class PostListView(ListView):\n"
         "    model = Post\n"
         "    template_name = 'blog/post_list.html'\n"
         "    context_object_name = 'posts'\n"
         "    paginate_by = 10\n\n"
         "    def get_queryset(self):\n"
         "        return Post.objects.filter(status='published')\n\n"
         "class PostDetailView(DetailView):\n"
         "    model = Post\n"
         "    template_name = 'blog/post_detail.html'\n\n"
         "class PostCreateView(CreateView):\n"
         "    model = Post\n"
         "    fields = ['title', 'body', 'status']\n"
         "    template_name = 'blog/post_form.html'\n"
         "    success_url = reverse_lazy('post_list')\n\n"
         "class PostDeleteView(DeleteView):\n"
         "    model = Post\n"
         "    template_name = 'blog/post_confirm_delete.html'\n"
         "    success_url = reverse_lazy('post_list')"
     )},

    # ── URLS ───────────────────────────────────────────────────────────────────
    {"chapter_slug": "urls", "order": 1, "section_type": "theory", "heading": "URL Configuration",
     "content": (
         "Django's URL dispatcher maps URL patterns to view functions.\n\n"
         "URL Pattern Converters:\n"
         "• <int:pk> — captures an integer\n"
         "• <str:name> — captures a string\n"
         "• <slug:slug> — captures a slug\n"
         "• <uuid:id> — captures a UUID\n"
         "• <path:subpath> — full path with slashes\n\n"
         "Always name your URLs so you can reference them in templates "
         "and views without hardcoding paths."
     ), "code": ""},

    {"chapter_slug": "urls", "order": 2, "section_type": "code", "heading": "URL Configuration Example",
     "content": "", "code": (
         "# mysite/urls.py  (project-level)\n"
         "from django.contrib import admin\n"
         "from django.urls import path, include\n\n"
         "urlpatterns = [\n"
         "    path('admin/', admin.site.urls),\n"
         "    path('blog/', include('blog.urls')),\n"
         "    path('accounts/', include('django.contrib.auth.urls')),\n"
         "]\n\n\n"
         "# blog/urls.py  (app-level)\n"
         "from django.urls import path\n"
         "from . import views\n\n"
         "app_name = 'blog'\n\n"
         "urlpatterns = [\n"
         "    path('',                     views.PostListView.as_view(),   name='post_list'),\n"
         "    path('<slug:slug>/',          views.PostDetailView.as_view(), name='post_detail'),\n"
         "    path('new/',                 views.PostCreateView.as_view(), name='create_post'),\n"
         "    path('<slug:slug>/edit/',    views.PostUpdateView.as_view(), name='update_post'),\n"
         "    path('<slug:slug>/delete/',  views.PostDeleteView.as_view(), name='delete_post'),\n"
         "]\n\n"
         "# In templates:\n"
         "# {% url 'blog:post_list' %}\n"
         "# {% url 'blog:post_detail' slug=post.slug %}"
     )},

    # ── TEMPLATES ──────────────────────────────────────────────────────────────
    {"chapter_slug": "templates", "order": 1, "section_type": "theory", "heading": "Django Template Language (DTL)",
     "content": (
         "Templates are HTML files with special DTL tags for dynamic content.\n\n"
         "DTL Syntax:\n"
         "• {{ variable }} — output a value\n"
         "• {% tag %} — logic tags\n"
         "• {# comment #} — template comments\n"
         "• {{ value|filter }} — apply a filter\n\n"
         "Common Tags:\n"
         "• {% if %} {% elif %} {% else %} {% endif %}\n"
         "• {% for item in list %} {% endfor %}\n"
         "• {% block name %} {% endblock %}\n"
         "• {% extends 'base.html' %}\n"
         "• {% include 'partial.html' %}\n"
         "• {% url 'name' %}\n"
         "• {% static 'path' %}\n"
         "• {% csrf_token %}"
     ), "code": ""},

    {"chapter_slug": "templates", "order": 2, "section_type": "code", "heading": "Base Template & Inheritance",
     "content": "", "code": (
         "{% load static %}\n"
         "<!DOCTYPE html>\n"
         "<html>\n"
         "<head>\n"
         "  <title>{% block title %}My Site{% endblock %}</title>\n"
         "  <link rel=\"stylesheet\" href=\"{% static 'css/style.css' %}\">\n"
         "</head>\n"
         "<body>\n"
         "  <nav>\n"
         "    <a href=\"{% url 'blog:post_list' %}\">Home</a>\n"
         "    {% if user.is_authenticated %}\n"
         "      Hello, {{ user.username }}!\n"
         "    {% else %}\n"
         "      <a href=\"{% url 'login' %}\">Login</a>\n"
         "    {% endif %}\n"
         "  </nav>\n"
         "  {% block content %}{% endblock %}\n"
         "</body>\n"
         "</html>\n\n\n"
         "{# child template #}\n"
         "{% extends 'base.html' %}\n"
         "{% block title %}Blog Posts{% endblock %}\n"
         "{% block content %}\n"
         "<h1>All Posts</h1>\n"
         "{% for post in posts %}\n"
         "  <h2><a href=\"{% url 'blog:post_detail' slug=post.slug %}\">{{ post.title }}</a></h2>\n"
         "  <p>{{ post.body|truncatewords:30 }}</p>\n"
         "{% empty %}\n"
         "  <p>No posts yet.</p>\n"
         "{% endfor %}\n"
         "{% endblock %}"
     )},

    {"chapter_slug": "templates", "order": 3, "section_type": "code", "heading": "Common Template Filters",
     "content": "", "code": (
         "{{ post.title|upper }}              {# UPPERCASE #}\n"
         "{{ post.title|lower }}              {# lowercase #}\n"
         "{{ post.title|truncatewords:10 }}   {# First 10 words #}\n"
         "{{ post.body|linebreaks }}          {# newline to <p> tags #}\n"
         "{{ post.body|safe }}                {# render raw HTML #}\n"
         "{{ post.body|striptags }}           {# strip HTML tags #}\n"
         "{{ post.created_at|date:\"Y-m-d\" }} {# 2024-01-15 #}\n"
         "{{ post.created_at|timesince }}     {# 3 days ago #}\n"
         "{{ items|length }}                  {# count of items #}\n"
         "{{ value|default:\"N/A\" }}          {# fallback value #}\n"
         "{{ price|floatformat:2 }}           {# 9.50 #}"
     )},

    # ── FORMS ──────────────────────────────────────────────────────────────────
    {"chapter_slug": "forms", "order": 1, "section_type": "theory", "heading": "Django Forms",
     "content": (
         "Django forms handle HTML rendering, validation, and error display automatically.\n\n"
         "Two types:\n"
         "• forms.Form — Standalone, not tied to a model. For contact, search, login.\n"
         "• forms.ModelForm — Auto-generates fields from a model. Perfect for create/update.\n\n"
         "Form Workflow:\n"
         "1. Define the form class\n"
         "2. Instantiate in view (empty for GET, with data for POST)\n"
         "3. Call form.is_valid() to validate\n"
         "4. Access form.cleaned_data for safe values\n"
         "5. Render with {{ form }} in template"
     ), "code": ""},

    {"chapter_slug": "forms", "order": 2, "section_type": "code", "heading": "Form & ModelForm",
     "content": "", "code": (
         "# blog/forms.py\n"
         "from django import forms\n"
         "from .models import Post\n\n"
         "class ContactForm(forms.Form):\n"
         "    name    = forms.CharField(max_length=100)\n"
         "    email   = forms.EmailField()\n"
         "    message = forms.CharField(widget=forms.Textarea, min_length=10)\n\n"
         "    def clean_email(self):\n"
         "        email = self.cleaned_data['email']\n"
         "        if 'spam' in email:\n"
         "            raise forms.ValidationError('Invalid email.')\n"
         "        return email\n\n\n"
         "class PostForm(forms.ModelForm):\n"
         "    class Meta:\n"
         "        model = Post\n"
         "        fields = ['title', 'body', 'category', 'status']\n"
         "        widgets = {\n"
         "            'title': forms.TextInput(attrs={'class': 'form-control'}),\n"
         "            'body':  forms.Textarea(attrs={'rows': 10}),\n"
         "        }\n\n\n"
         "# views.py\n"
         "def contact(request):\n"
         "    if request.method == 'POST':\n"
         "        form = ContactForm(request.POST)\n"
         "        if form.is_valid():\n"
         "            name = form.cleaned_data['name']\n"
         "            return redirect('thank_you')\n"
         "    else:\n"
         "        form = ContactForm()\n"
         "    return render(request, 'contact.html', {'form': form})"
     )},

    {"chapter_slug": "forms", "order": 3, "section_type": "code", "heading": "Form in Template",
     "content": "", "code": (
         "<form method=\"post\">\n"
         "  {% csrf_token %}\n\n"
         "  {# Render all fields at once #}\n"
         "  {{ form.as_p }}\n\n"
         "  {# Or render field by field #}\n"
         "  <div class=\"field\">\n"
         "    {{ form.name.label_tag }}\n"
         "    {{ form.name }}\n"
         "    {% if form.name.errors %}\n"
         "      {% for error in form.name.errors %}\n"
         "        <p class=\"error\">{{ error }}</p>\n"
         "      {% endfor %}\n"
         "    {% endif %}\n"
         "  </div>\n\n"
         "  <button type=\"submit\">Submit</button>\n"
         "</form>"
     )},

    # ── ADMIN ──────────────────────────────────────────────────────────────────
    {"chapter_slug": "admin", "order": 1, "section_type": "theory", "heading": "The Admin Interface",
     "content": (
         "One of Django's most powerful features is the automatic admin interface. "
         "Register your models and get a full CRUD panel with zero extra code.\n\n"
         "Features:\n"
         "• List, create, edit, delete any registered model\n"
         "• Search, filter, and sort records\n"
         "• Inline editing of related models\n"
         "• Bulk actions\n"
         "• Permission-based access control\n\n"
         "Access at: http://localhost:8000/admin/\n\n"
         "Create superuser: python manage.py createsuperuser"
     ), "code": ""},

    {"chapter_slug": "admin", "order": 2, "section_type": "commands", "heading": "Admin Setup Commands",
     "content": "", "code": ""},

    {"chapter_slug": "admin", "order": 3, "section_type": "code", "heading": "Customising the Admin",
     "content": "", "code": (
         "# blog/admin.py\n"
         "from django.contrib import admin\n"
         "from .models import Post, Category\n\n"
         "admin.site.register(Category)\n\n"
         "@admin.register(Post)\n"
         "class PostAdmin(admin.ModelAdmin):\n"
         "    list_display  = ['title', 'author', 'status', 'created_at']\n"
         "    list_filter   = ['status', 'created_at', 'author']\n"
         "    search_fields = ['title', 'body']\n"
         "    prepopulated_fields = {'slug': ('title',)}\n"
         "    date_hierarchy = 'created_at'\n"
         "    ordering       = ['-created_at']\n"
         "    readonly_fields = ['created_at', 'updated_at']\n"
         "    fieldsets = (\n"
         "        ('Content', {'fields': ('title', 'slug', 'author', 'body')}),\n"
         "        ('Meta',    {'fields': ('category', 'status'), 'classes': ('collapse',)}),\n"
         "    )\n"
         "    actions = ['publish_posts']\n\n"
         "    def publish_posts(self, request, queryset):\n"
         "        queryset.update(status='published')\n"
         "        self.message_user(request, f'{queryset.count()} posts published.')\n"
         "    publish_posts.short_description = 'Mark selected as published'"
     )},

    # ── AUTH ───────────────────────────────────────────────────────────────────
    {"chapter_slug": "auth", "order": 1, "section_type": "theory", "heading": "Built-in Authentication",
     "content": (
         "Django includes a complete authentication system:\n"
         "• User login and logout\n"
         "• Password hashing (PBKDF2 by default)\n"
         "• Password reset via email\n"
         "• User groups and permissions\n\n"
         "User model fields: username, email, password, first_name, last_name, "
         "is_active, is_staff, is_superuser, date_joined\n\n"
         "Protecting Views:\n"
         "• @login_required — FBV decorator\n"
         "• LoginRequiredMixin — CBV mixin\n"
         "• request.user.is_authenticated — check in view"
     ), "code": ""},

    {"chapter_slug": "auth", "order": 2, "section_type": "code", "heading": "Auth Views & Decorators",
     "content": "", "code": (
         "# urls.py\n"
         "urlpatterns = [\n"
         "    path('accounts/', include('django.contrib.auth.urls')),\n"
         "    path('register/', views.register, name='register'),\n"
         "]\n\n"
         "# settings.py\n"
         "LOGIN_URL = '/accounts/login/'\n"
         "LOGIN_REDIRECT_URL = '/'\n"
         "LOGOUT_REDIRECT_URL = '/'\n\n\n"
         "# views.py\n"
         "from django.contrib.auth.decorators import login_required\n"
         "from django.contrib.auth.mixins import LoginRequiredMixin\n"
         "from django.contrib.auth import login\n"
         "from django.contrib.auth.models import User\n\n"
         "@login_required\n"
         "def dashboard(request):\n"
         "    return render(request, 'dashboard.html')\n\n"
         "class DashboardView(LoginRequiredMixin, ListView):\n"
         "    model = Post\n\n"
         "def register(request):\n"
         "    if request.method == 'POST':\n"
         "        user = User.objects.create_user(\n"
         "            username=request.POST['username'],\n"
         "            password=request.POST['password'],\n"
         "        )\n"
         "        login(request, user)\n"
         "        return redirect('/')\n"
         "    return render(request, 'register.html')"
     )},

    # ── STATIC / MEDIA ─────────────────────────────────────────────────────────
    {"chapter_slug": "staticmedia", "order": 1, "section_type": "theory", "heading": "Static vs Media Files",
     "content": (
         "Static Files — CSS, JavaScript, images you include in your project.\n\n"
         "Media Files — Files uploaded by users: profile photos, post images.\n\n"
         "In Development: Django serves both when DEBUG=True.\n\n"
         "In Production: Never use Django to serve static/media files. "
         "Use Nginx or a CDN (AWS S3). Run collectstatic to gather all files into one folder."
     ), "code": ""},

    {"chapter_slug": "staticmedia", "order": 2, "section_type": "commands",
     "heading": "Static File Commands", "content": "", "code": ""},

    {"chapter_slug": "staticmedia", "order": 3, "section_type": "code", "heading": "Configuration",
     "content": "", "code": (
         "# settings.py\n"
         "STATIC_URL = '/static/'\n"
         "STATICFILES_DIRS = [BASE_DIR / 'static']\n"
         "STATIC_ROOT = BASE_DIR / 'staticfiles'\n\n"
         "MEDIA_URL = '/media/'\n"
         "MEDIA_ROOT = BASE_DIR / 'media'\n\n\n"
         "# urls.py — serve media in development\n"
         "from django.conf import settings\n"
         "from django.conf.urls.static import static\n\n"
         "urlpatterns = [...] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\n\n\n"
         "# templates\n"
         "{% load static %}\n"
         "<link rel=\"stylesheet\" href=\"{% static 'css/style.css' %}\">\n"
         "<img src=\"{% static 'images/logo.png' %}\" alt=\"Logo\">\n\n"
         "{% if post.image %}\n"
         "    <img src=\"{{ post.image.url }}\" alt=\"{{ post.title }}\">\n"
         "{% endif %}"
     )},

    # ── DRF ────────────────────────────────────────────────────────────────────
    {"chapter_slug": "drf", "order": 1, "section_type": "theory", "heading": "Building APIs with DRF",
     "content": (
         "Django REST Framework (DRF) is the standard library for Web APIs in Django.\n\n"
         "It adds:\n"
         "• Serializers — Convert model instances to/from JSON\n"
         "• API Views — Function and class based API views\n"
         "• ViewSets — Group related API views together\n"
         "• Routers — Auto-generate API URLs from ViewSets\n"
         "• Authentication — Token, Session, JWT\n"
         "• Browsable API — Auto-generated HTML interface for testing"
     ), "code": ""},

    {"chapter_slug": "drf", "order": 2, "section_type": "commands",
     "heading": "Install DRF", "content": "", "code": ""},

    {"chapter_slug": "drf", "order": 3, "section_type": "code",
     "heading": "Serializers, ViewSets & Router", "content": "", "code": (
         "# blog/serializers.py\n"
         "from rest_framework import serializers\n"
         "from .models import Post\n\n"
         "class PostSerializer(serializers.ModelSerializer):\n"
         "    author_name = serializers.CharField(source='author.username', read_only=True)\n\n"
         "    class Meta:\n"
         "        model = Post\n"
         "        fields = ['id', 'title', 'slug', 'body', 'status', 'author_name', 'created_at']\n"
         "        read_only_fields = ['created_at']\n\n\n"
         "# blog/views.py\n"
         "from rest_framework import viewsets, permissions\n"
         "from .serializers import PostSerializer\n\n"
         "class PostViewSet(viewsets.ModelViewSet):\n"
         "    queryset = Post.objects.filter(status='published')\n"
         "    serializer_class = PostSerializer\n"
         "    permission_classes = [permissions.IsAuthenticatedOrReadOnly]\n\n"
         "    def perform_create(self, serializer):\n"
         "        serializer.save(author=self.request.user)\n\n\n"
         "# blog/urls.py\n"
         "from rest_framework.routers import DefaultRouter\n"
         "router = DefaultRouter()\n"
         "router.register('posts', PostViewSet, basename='post')\n\n"
         "urlpatterns = [path('api/', include(router.urls))]\n"
         "# Generates:\n"
         "# GET/POST              /api/posts/\n"
         "# GET/PUT/PATCH/DELETE  /api/posts/{id}/"
     )},
]

COMMANDS = {
    # section identified by (chapter_slug, section_heading)
    ("setup",       "Installation Commands"): [
        ("python --version",                              "Check Python version (need 3.8+)"),
        ("pip --version",                                 "Check pip version"),
        ("python -m venv venv",                           "Create a virtual environment"),
        ("source venv/bin/activate",                      "Activate venv (Linux/Mac)"),
        ("venv\\Scripts\\activate",                       "Activate venv (Windows)"),
        ("pip install django",                            "Install Django inside venv"),
        ("django-admin --version",                        "Verify Django installation"),
        ("django-admin startproject mysite",              "Create a new Django project"),
        ("python manage.py startapp blog",                "Create a new app"),
        ("python manage.py runserver",                    "Start the development server"),
        ("pip freeze > requirements.txt",                 "Save dependencies to file"),
        ("pip install -r requirements.txt",               "Install from requirements file"),
    ],
    ("models",      "Migration Commands"): [
        ("python manage.py makemigrations",               "Generate migration files from model changes"),
        ("python manage.py migrate",                      "Apply all pending migrations to DB"),
        ("python manage.py showmigrations",               "Show all migrations and their status"),
        ("python manage.py sqlmigrate blog 0001",         "Show SQL for a specific migration"),
        ("python manage.py migrate blog zero",            "Unapply all migrations for an app"),
    ],
    ("admin",       "Admin Setup Commands"): [
        ("python manage.py createsuperuser",              "Create an admin user account"),
        ("python manage.py changepassword username",      "Change a user's password"),
    ],
    ("staticmedia", "Static File Commands"): [
        ("python manage.py collectstatic",                "Collect all static files into STATIC_ROOT"),
        ("python manage.py findstatic style.css",         "Find where a static file comes from"),
    ],
    ("drf",         "Install DRF"): [
        ("pip install djangorestframework",               "Install Django REST Framework"),
        ("pip install djangorestframework-simplejwt",     "Install JWT authentication for DRF"),
    ],
}


CHAPTERS.extend([
    {"order": 2, "slug": "history", "icon": "H", "title": "Django History & Philosophy", "color": "#2ecc71"},
    {"order": 4, "slug": "request-response", "icon": "R", "title": "Request & Response Cycle", "color": "#8e44ad"},
    {"order": 25, "slug": "middleware", "icon": "M", "title": "Middleware", "color": "#d35400"},
    {"order": 12, "slug": "querysets", "icon": "Q", "title": "Advanced QuerySets", "color": "#27ae60"},
    {"order": 13, "slug": "migrations-deep", "icon": "D", "title": "Migrations Deep Dive", "color": "#34495e"},
    {"order": 26, "slug": "signals", "icon": "S", "title": "Signals", "color": "#c0392b"},
    {"order": 20, "slug": "sessions-messages", "icon": "U", "title": "Sessions & Messages", "color": "#16a085"},
    {"order": 30, "slug": "security", "icon": "X", "title": "Security Checklist", "color": "#e74c3c"},
    {"order": 29, "slug": "testing", "icon": "T", "title": "Testing Django Apps", "color": "#2980b9"},
    {"order": 36, "slug": "deployment", "icon": "P", "title": "Deployment & Production", "color": "#7f8c8d"},
    {"order": 33, "slug": "performance", "icon": "F", "title": "Performance & Caching", "color": "#f1c40f"},
    {"order": 34, "slug": "async", "icon": "A", "title": "Async Django", "color": "#9b59b6"},
    {"order": 35, "slug": "i18n", "icon": "I", "title": "Internationalization", "color": "#1abc9c"},
    {"order": 6, "slug": "architecture", "icon": "B", "title": "Project Architecture", "color": "#3498db"},
])

SECTIONS.extend([
    {"chapter_slug": "history", "order": 1, "section_type": "theory", "heading": "Where Django Came From",
     "content": (
         "Django began at the Lawrence Journal-World newspaper in Kansas, where developers needed to build "
         "database-backed news sites quickly and reliably. It was released publicly in 2005 and became known "
         "for its practical batteries-included approach.\n\n"
         "Important ideas:\n"
         "- Build secure sites quickly without repeating common web plumbing.\n"
         "- Prefer explicit, readable Python over hidden magic.\n"
         "- Include production-grade tools: ORM, admin, auth, forms, sessions, templates, security middleware.\n"
         "- Keep apps reusable so one project can be built from many focused components.\n\n"
         "Django is not only a framework. It is a set of opinions about maintainable web development."
     ), "code": ""},
    {"chapter_slug": "history", "order": 2, "section_type": "theory", "heading": "Design Philosophy",
     "content": (
         "Django's philosophy can be summarized as speed with discipline.\n\n"
         "- DRY: do not repeat yourself.\n"
         "- Loose coupling: URLs, views, models, and templates should remain separate.\n"
         "- Explicit is better than implicit: project behavior should be visible in code.\n"
         "- Consistency: common patterns should look the same across apps.\n"
         "- Security by default: common protections are built in, but developers must configure production carefully.\n\n"
         "A strong Django project feels boring in a good way: predictable folders, small apps, clear models, "
         "tested views, and settings that separate development from production."
     ), "code": ""},

    {"chapter_slug": "request-response", "order": 1, "section_type": "theory", "heading": "The Full Request Flow",
     "content": (
         "Every Django page starts with an HTTP request and ends with an HTTP response.\n\n"
         "Flow:\n"
         "1. Browser sends a request.\n"
         "2. Web server forwards it to Django through WSGI or ASGI.\n"
         "3. Middleware runs before the view.\n"
         "4. URL resolver chooses a view.\n"
         "5. View reads request data, talks to models/services, and returns a response.\n"
         "6. Middleware can modify the response.\n"
         "7. Browser receives HTML, JSON, redirect, file, or error response.\n\n"
         "Understanding this cycle makes debugging much easier."
     ), "code": ""},
    {"chapter_slug": "request-response", "order": 2, "section_type": "code", "heading": "Common Response Types",
     "content": "", "code": (
         "from django.http import HttpResponse, JsonResponse, FileResponse\n"
         "from django.shortcuts import render, redirect\n\n"
         "def html_page(request):\n"
         "    return render(request, 'blog/home.html', {'title': 'Home'})\n\n"
         "def text_page(request):\n"
         "    return HttpResponse('Hello Django')\n\n"
         "def api_status(request):\n"
         "    return JsonResponse({'ok': True})\n\n"
         "def go_home(request):\n"
         "    return redirect('blog:home')\n\n"
         "def download_report(request):\n"
         "    return FileResponse(open('report.pdf', 'rb'), as_attachment=True)"
     )},

    {"chapter_slug": "middleware", "order": 1, "section_type": "theory", "heading": "What Middleware Does",
     "content": (
         "Middleware is a chain of hooks around every request and response. It is used for security, sessions, "
         "authentication, messages, redirects, logging, compression, and custom cross-cutting behavior.\n\n"
         "Examples from Django:\n"
         "- SecurityMiddleware: HTTPS and browser security headers.\n"
         "- SessionMiddleware: attaches request.session.\n"
         "- CsrfViewMiddleware: protects unsafe form submissions.\n"
         "- AuthenticationMiddleware: attaches request.user.\n\n"
         "Use middleware for behavior that applies to many views. Do not put page-specific business logic there."
     ), "code": ""},
    {"chapter_slug": "middleware", "order": 2, "section_type": "code", "heading": "Custom Middleware",
     "content": "", "code": (
         "# core/middleware.py\n"
         "import time\n"
         "import logging\n\n"
         "logger = logging.getLogger(__name__)\n\n"
         "class RequestTimingMiddleware:\n"
         "    def __init__(self, get_response):\n"
         "        self.get_response = get_response\n\n"
         "    def __call__(self, request):\n"
         "        started = time.perf_counter()\n"
         "        response = self.get_response(request)\n"
         "        elapsed_ms = (time.perf_counter() - started) * 1000\n"
         "        logger.info('%s %s %.2fms', request.method, request.path, elapsed_ms)\n"
         "        return response\n\n"
         "# settings.py\n"
         "MIDDLEWARE = [\n"
         "    'core.middleware.RequestTimingMiddleware',\n"
         "    # ... other middleware\n"
         "]"
     )},

    {"chapter_slug": "querysets", "order": 1, "section_type": "theory", "heading": "QuerySet Mastery",
     "content": (
         "QuerySets are lazy database queries. They do not usually hit the database until you iterate, slice, "
         "count, convert to list, or ask for a single result.\n\n"
         "Important concepts:\n"
         "- filter() narrows results; exclude() removes results.\n"
         "- select_related() joins foreign keys and one-to-one relations.\n"
         "- prefetch_related() optimizes many-to-many and reverse foreign keys.\n"
         "- annotate() adds calculated fields.\n"
         "- aggregate() returns summary values.\n"
         "- values() and values_list() return dictionaries or tuples instead of model instances."
     ), "code": ""},
    {"chapter_slug": "querysets", "order": 2, "section_type": "code", "heading": "Advanced ORM Patterns",
     "content": "", "code": (
         "from django.db.models import Count, Q, Avg, F\n"
         "from blog.models import Post, Category\n\n"
         "# Avoid N+1 queries for foreign keys\n"
         "posts = Post.objects.select_related('author', 'category')\n\n"
         "# Avoid N+1 queries for many-to-many or reverse relations\n"
         "categories = Category.objects.prefetch_related('posts')\n\n"
         "# Search multiple fields\n"
         "results = Post.objects.filter(Q(title__icontains='django') | Q(body__icontains='django'))\n\n"
         "# Add calculated values\n"
         "categories = Category.objects.annotate(post_count=Count('posts'))\n\n"
         "# Database-side update\n"
         "Post.objects.filter(status='draft').update(view_count=F('view_count') + 1)\n\n"
         "# Summary value\n"
         "average_views = Post.objects.aggregate(avg=Avg('view_count'))"
     )},

    {"chapter_slug": "migrations-deep", "order": 1, "section_type": "theory", "heading": "How Migrations Work",
     "content": (
         "Migrations are version control for your database schema. Django compares your model state with the "
         "last recorded migration state, creates migration files, then applies those files to the database.\n\n"
         "Good migration habits:\n"
         "- Review migration files before committing.\n"
         "- Keep data migrations small and reversible when possible.\n"
         "- Avoid editing old migrations after other people have used them.\n"
         "- For large tables, be careful with non-null fields, indexes, and data backfills.\n"
         "- Use separate schema and data migrations for risky production changes."
     ), "code": ""},
    {"chapter_slug": "migrations-deep", "order": 2, "section_type": "code", "heading": "Data Migration Pattern",
     "content": "", "code": (
         "from django.db import migrations\n\n"
         "def forwards(apps, schema_editor):\n"
         "    Category = apps.get_model('blog', 'Category')\n"
         "    Category.objects.get_or_create(name='Django', slug='django')\n\n"
         "def backwards(apps, schema_editor):\n"
         "    Category = apps.get_model('blog', 'Category')\n"
         "    Category.objects.filter(slug='django').delete()\n\n"
         "class Migration(migrations.Migration):\n"
         "    dependencies = [\n"
         "        ('blog', '0001_initial'),\n"
         "    ]\n\n"
         "    operations = [\n"
         "        migrations.RunPython(forwards, backwards),\n"
         "    ]"
     )},

    {"chapter_slug": "signals", "order": 1, "section_type": "theory", "heading": "Signals Explained",
     "content": (
         "Signals let parts of an app react when something happens elsewhere, such as a model being saved. "
         "Common signals include pre_save, post_save, pre_delete, post_delete, and m2m_changed.\n\n"
         "Use signals carefully. They are useful for side effects like creating a profile after user creation, "
         "but they can hide behavior and make debugging harder. If the workflow is important, a service function "
         "or explicit view logic is often clearer."
     ), "code": ""},
    {"chapter_slug": "signals", "order": 2, "section_type": "code", "heading": "Create Profile on Signup",
     "content": "", "code": (
         "# accounts/signals.py\n"
         "from django.contrib.auth import get_user_model\n"
         "from django.db.models.signals import post_save\n"
         "from django.dispatch import receiver\n"
         "from .models import Profile\n\n"
         "User = get_user_model()\n\n"
         "@receiver(post_save, sender=User)\n"
         "def create_profile(sender, instance, created, **kwargs):\n"
         "    if created:\n"
         "        Profile.objects.create(user=instance)\n\n"
         "# accounts/apps.py\n"
         "class AccountsConfig(AppConfig):\n"
         "    name = 'accounts'\n\n"
         "    def ready(self):\n"
         "        import accounts.signals"
     )},

    {"chapter_slug": "sessions-messages", "order": 1, "section_type": "theory", "heading": "Sessions, Cookies, and Messages",
     "content": (
         "Sessions store per-user state on the server side while keeping only a session key in the browser cookie. "
         "They are useful for carts, temporary preferences, onboarding state, and login tracking.\n\n"
         "Messages are one-time notifications stored between requests. They are perfect after redirects: "
         "success after saving, warning after validation, or info after logout."
     ), "code": ""},
    {"chapter_slug": "sessions-messages", "order": 2, "section_type": "code", "heading": "Using Sessions and Messages",
     "content": "", "code": (
         "from django.contrib import messages\n"
         "from django.shortcuts import redirect, render\n\n"
         "def choose_theme(request):\n"
         "    request.session['theme'] = 'dark'\n"
         "    messages.success(request, 'Theme saved.')\n"
         "    return redirect('settings')\n\n"
         "def settings_page(request):\n"
         "    theme = request.session.get('theme', 'light')\n"
         "    return render(request, 'settings.html', {'theme': theme})\n\n"
         "# template\n"
         "{% for message in messages %}\n"
         "  <p class=\"message {{ message.tags }}\">{{ message }}</p>\n"
         "{% endfor %}"
     )},

    {"chapter_slug": "security", "order": 1, "section_type": "theory", "heading": "Production Security Checklist",
     "content": (
         "Django ships with many security protections, but production safety depends on configuration.\n\n"
         "Checklist:\n"
         "- Set DEBUG=False.\n"
         "- Keep SECRET_KEY out of source code.\n"
         "- Set ALLOWED_HOSTS to real domains.\n"
         "- Use HTTPS and secure cookies.\n"
         "- Keep CSRF middleware enabled.\n"
         "- Avoid marking user content safe in templates.\n"
         "- Use parameterized ORM queries instead of raw SQL string formatting.\n"
         "- Update Django when security releases are published.\n"
         "- Configure logging and error monitoring."
     ), "code": ""},
    {"chapter_slug": "security", "order": 2, "section_type": "code", "heading": "Safer Production Settings",
     "content": "", "code": (
         "import os\n\n"
         "SECRET_KEY = os.environ['DJANGO_SECRET_KEY']\n"
         "DEBUG = os.environ.get('DJANGO_DEBUG') == '1'\n"
         "ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', '').split(',')\n\n"
         "CSRF_COOKIE_SECURE = True\n"
         "SESSION_COOKIE_SECURE = True\n"
         "SECURE_SSL_REDIRECT = True\n"
         "SECURE_HSTS_SECONDS = 31536000\n"
         "SECURE_HSTS_INCLUDE_SUBDOMAINS = True\n"
         "SECURE_HSTS_PRELOAD = True\n"
         "SECURE_REFERRER_POLICY = 'same-origin'\n"
         "X_FRAME_OPTIONS = 'DENY'"
     )},

    {"chapter_slug": "testing", "order": 1, "section_type": "theory", "heading": "What to Test",
     "content": (
         "Django tests protect your app from regressions. Start with behavior that users depend on.\n\n"
         "Test layers:\n"
         "- Model tests: methods, validation, constraints, string output.\n"
         "- View tests: status codes, redirects, templates, context data.\n"
         "- Form tests: valid data, invalid data, error messages.\n"
         "- Permission tests: anonymous user, normal user, staff user.\n"
         "- API tests: JSON shape, status codes, authentication.\n\n"
         "A portfolio project looks much stronger with even a small but meaningful test suite."
     ), "code": ""},
    {"chapter_slug": "testing", "order": 2, "section_type": "code", "heading": "Example Django Tests",
     "content": "", "code": (
         "from django.test import TestCase\n"
         "from django.urls import reverse\n"
         "from .models import Post\n\n"
         "class PostTests(TestCase):\n"
         "    def setUp(self):\n"
         "        self.post = Post.objects.create(title='Hello', slug='hello', body='Body')\n\n"
         "    def test_post_string(self):\n"
         "        self.assertEqual(str(self.post), 'Hello')\n\n"
         "    def test_post_detail_page(self):\n"
         "        response = self.client.get(reverse('blog:post_detail', kwargs={'slug': 'hello'}))\n"
         "        self.assertEqual(response.status_code, 200)\n"
         "        self.assertContains(response, 'Hello')"
     )},

    {"chapter_slug": "deployment", "order": 1, "section_type": "theory", "heading": "From Localhost to Production",
     "content": (
         "Production Django usually includes a process manager, a WSGI or ASGI server, a real database, static "
         "file hosting, environment variables, logging, backups, and monitoring.\n\n"
         "Common choices:\n"
         "- Gunicorn or uWSGI for WSGI apps.\n"
         "- Uvicorn or Daphne for ASGI apps.\n"
         "- PostgreSQL for production databases.\n"
         "- Nginx, WhiteNoise, S3, or CDN for static files.\n"
         "- GitHub Actions or another CI system for tests and deploys."
     ), "code": ""},
    {"chapter_slug": "deployment", "order": 2, "section_type": "commands", "heading": "Production Commands",
     "content": "", "code": ""},

    {"chapter_slug": "performance", "order": 1, "section_type": "theory", "heading": "Performance Basics",
     "content": (
         "Most Django performance issues come from too many database queries, missing indexes, slow templates, "
         "uncached expensive work, or sending too much data.\n\n"
         "First steps:\n"
         "- Measure before optimizing.\n"
         "- Use select_related and prefetch_related.\n"
         "- Add indexes for common filters and ordering.\n"
         "- Cache expensive pages or fragments.\n"
         "- Paginate large lists.\n"
         "- Move slow background tasks out of request/response flow."
     ), "code": ""},
    {"chapter_slug": "performance", "order": 2, "section_type": "code", "heading": "Caching Examples",
     "content": "", "code": (
         "from django.core.cache import cache\n"
         "from django.views.decorators.cache import cache_page\n\n"
         "@cache_page(60 * 15)\n"
         "def homepage(request):\n"
         "    return render(request, 'home.html')\n\n"
         "def expensive_stats():\n"
         "    value = cache.get('stats')\n"
         "    if value is None:\n"
         "        value = calculate_stats()\n"
         "        cache.set('stats', value, 300)\n"
         "    return value"
     )},

    {"chapter_slug": "async", "order": 1, "section_type": "theory", "heading": "Async in Django",
     "content": (
         "Django supports both sync and async views. Async is useful for handling many waiting operations, "
         "especially network I/O. It does not automatically make CPU-heavy code faster.\n\n"
         "Know the boundary:\n"
         "- Sync views are still normal and often best.\n"
         "- Async views must avoid blocking calls.\n"
         "- Many ORM operations are traditionally sync, though Django has added async ORM methods over time.\n"
         "- Use ASGI for true async serving."
     ), "code": ""},
    {"chapter_slug": "async", "order": 2, "section_type": "code", "heading": "Async View Example",
     "content": "", "code": (
         "import httpx\n"
         "from django.http import JsonResponse\n\n"
         "async def external_status(request):\n"
         "    async with httpx.AsyncClient() as client:\n"
         "        response = await client.get('https://example.com/status')\n"
         "    return JsonResponse({'status': response.status_code})"
     )},

    {"chapter_slug": "i18n", "order": 1, "section_type": "theory", "heading": "Translations and Time Zones",
     "content": (
         "Internationalization lets one Django project support multiple languages and locales. Localization "
         "formats dates, numbers, and times for users. Time zone support helps store datetimes consistently "
         "while displaying them correctly for each user.\n\n"
         "Core tools:\n"
         "- gettext and gettext_lazy for Python strings.\n"
         "- trans and blocktrans in templates.\n"
         "- makemessages and compilemessages commands.\n"
         "- USE_TZ=True to store aware datetimes."
     ), "code": ""},
    {"chapter_slug": "i18n", "order": 2, "section_type": "code", "heading": "Translation Examples",
     "content": "", "code": (
         "# models.py or forms.py\n"
         "from django.utils.translation import gettext_lazy as _\n\n"
         "class Product(models.Model):\n"
         "    name = models.CharField(_('name'), max_length=100)\n\n"
         "# template\n"
         "{% load i18n %}\n"
         "<h1>{% trans 'Welcome' %}</h1>\n"
         "{% blocktrans with name=user.username %}Hello {{ name }}{% endblocktrans %}"
     )},

    {"chapter_slug": "architecture", "order": 1, "section_type": "theory", "heading": "How to Structure Real Projects",
     "content": (
         "A maintainable Django project grows through clear boundaries. Apps should represent business areas, "
         "not random technical folders. Keep models close to their domain, keep views thin, and move complex "
         "workflows into services or model methods.\n\n"
         "Good structure:\n"
         "- config/: project settings, root URLs, ASGI/WSGI.\n"
         "- apps/accounts/: users, profiles, auth workflows.\n"
         "- apps/blog/: posts, categories, comments.\n"
         "- templates/: shared and app-specific templates.\n"
         "- static/: CSS, JavaScript, images.\n"
         "- tests/: behavior-focused tests.\n\n"
         "Avoid one huge app that owns everything."
     ), "code": ""},
    {"chapter_slug": "architecture", "order": 2, "section_type": "code", "heading": "Service Layer Example",
     "content": "", "code": (
         "# blog/services.py\n"
         "from django.db import transaction\n"
         "from .models import Post, AuditLog\n\n"
         "@transaction.atomic\n"
         "def publish_post(post: Post, user):\n"
         "    post.status = 'published'\n"
         "    post.published_by = user\n"
         "    post.save(update_fields=['status', 'published_by'])\n"
         "    AuditLog.objects.create(user=user, action='published_post', object_id=post.id)\n"
         "    return post\n\n"
         "# views.py\n"
         "def publish(request, pk):\n"
         "    post = get_object_or_404(Post, pk=pk)\n"
         "    publish_post(post, request.user)\n"
         "    return redirect(post)"
    )},
])

SECTIONS.extend([
    {"chapter_slug": "email", "order": 3, "section_type": "commands", "heading": "Email & Password Reset Commands",
     "content": "", "code": ""},
    {"chapter_slug": "management-commands", "order": 3, "section_type": "commands", "heading": "Management Command Commands",
     "content": "", "code": ""},
    {"chapter_slug": "channels", "order": 3, "section_type": "commands", "heading": "Channels Commands",
     "content": "", "code": ""},
    {"chapter_slug": "celery", "order": 3, "section_type": "commands", "heading": "Celery Commands",
     "content": "", "code": ""},
    {"chapter_slug": "docker", "order": 3, "section_type": "commands", "heading": "Docker Commands",
     "content": "", "code": ""},
    {"chapter_slug": "cicd", "order": 3, "section_type": "commands", "heading": "CI/CD Commands",
     "content": "", "code": ""},
])

COMMANDS.update({
    ("deployment", "Production Commands"): [
        ("python manage.py check --deploy", "Run Django's deployment security checklist"),
        ("python manage.py collectstatic", "Collect static files before deployment"),
        ("python manage.py migrate", "Apply database migrations on the production database"),
        ("gunicorn config.wsgi:application", "Run a WSGI Django app with Gunicorn"),
        ("uvicorn config.asgi:application", "Run an ASGI Django app with Uvicorn"),
    ],
})


CHAPTERS.extend([
    {"order": 18, "slug": "custom-user", "icon": "CU", "title": "Custom User Model", "color": "#2c3e50"},
    {"order": 19, "slug": "permissions", "icon": "PM", "title": "Permissions & Authorization", "color": "#8e44ad"},
    {"order": 22, "slug": "file-uploads", "icon": "UP", "title": "File Uploads & Storage", "color": "#3498db"},
    {"order": 23, "slug": "email", "icon": "EM", "title": "Email & Password Reset", "color": "#16a085"},
    {"order": 24, "slug": "pagination-search", "icon": "PS", "title": "Pagination, Search & Filtering", "color": "#f39c12"},
    {"order": 27, "slug": "management-commands", "icon": "MC", "title": "Custom Management Commands", "color": "#7f8c8d"},
    {"order": 28, "slug": "transactions", "icon": "TX", "title": "Transactions & Database Integrity", "color": "#c0392b"},
    {"order": 16, "slug": "advanced-admin", "icon": "AA", "title": "Advanced Admin", "color": "#27ae60"},
    {"order": 9, "slug": "cbv-deep", "icon": "CB", "title": "Class-Based Views Deep Dive", "color": "#d35400"},
    {"order": 32, "slug": "drf-advanced", "icon": "DA", "title": "Advanced DRF", "color": "#2980b9"},
    {"order": 43, "slug": "channels", "icon": "WS", "title": "WebSockets with Channels", "color": "#9b59b6"},
    {"order": 42, "slug": "celery", "icon": "CE", "title": "Celery & Background Tasks", "color": "#44b78b"},
    {"order": 37, "slug": "docker", "icon": "DK", "title": "Docker for Django", "color": "#1abc9c"},
    {"order": 38, "slug": "cicd", "icon": "CI", "title": "CI/CD with GitHub Actions", "color": "#34495e"},
    {"order": 39, "slug": "logging-monitoring", "icon": "LM", "title": "Logging & Monitoring", "color": "#e67e22"},
    {"order": 40, "slug": "postgres", "icon": "PG", "title": "PostgreSQL Features", "color": "#336791"},
    {"order": 41, "slug": "multidb", "icon": "DB", "title": "Multiple Databases", "color": "#6c5ce7"},
    {"order": 44, "slug": "internals", "icon": "IN", "title": "Django Internals", "color": "#00b894"},
])

SECTIONS.extend([
    {"chapter_slug": "custom-user", "order": 1, "section_type": "theory", "heading": "Why Custom User Models Matter",
     "content": (
         "Django includes a built-in User model, but real projects often need email login, profile fields, "
         "or organization-specific identity rules. The safest practice is to create a custom user model at "
         "the beginning of a project, before the first migration.\n\n"
         "Two common approaches:\n"
         "- AbstractUser: keeps Django's username/password behavior and lets you add fields.\n"
         "- AbstractBaseUser: full control, but more work because you define login fields and manager methods.\n\n"
         "For most projects, AbstractUser is the best starting point."
     ), "code": ""},
    {"chapter_slug": "custom-user", "order": 2, "section_type": "code", "heading": "AbstractUser Example",
     "content": "", "code": (
         "# accounts/models.py\n"
         "from django.contrib.auth.models import AbstractUser\n"
         "from django.db import models\n\n"
         "class User(AbstractUser):\n"
         "    bio = models.TextField(blank=True)\n"
         "    avatar = models.ImageField(upload_to='avatars/', blank=True)\n\n"
         "# settings.py\n"
         "AUTH_USER_MODEL = 'accounts.User'\n\n"
         "# use in relations\n"
         "from django.conf import settings\n"
         "author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)"
     )},

    {"chapter_slug": "permissions", "order": 1, "section_type": "theory", "heading": "Authentication vs Authorization",
     "content": (
         "Authentication asks: who is this user? Authorization asks: what is this user allowed to do?\n\n"
         "Django authorization tools:\n"
         "- is_authenticated: user has logged in.\n"
         "- is_staff: user can access admin if permissions allow.\n"
         "- is_superuser: user bypasses normal permission checks.\n"
         "- Groups: reusable permission bundles.\n"
         "- Model permissions: add, change, delete, view.\n"
         "- Custom permissions: app-specific actions.\n\n"
         "For object-level permissions, use custom checks or a package such as django-guardian."
     ), "code": ""},
    {"chapter_slug": "permissions", "order": 2, "section_type": "code", "heading": "Permission Checks",
     "content": "", "code": (
         "from django.contrib.auth.decorators import permission_required\n"
         "from django.contrib.auth.mixins import PermissionRequiredMixin\n\n"
         "@permission_required('blog.change_post', raise_exception=True)\n"
         "def edit_post(request, pk):\n"
         "    ...\n\n"
         "class PostUpdateView(PermissionRequiredMixin, UpdateView):\n"
         "    model = Post\n"
         "    fields = ['title', 'body']\n"
         "    permission_required = 'blog.change_post'\n\n"
         "# models.py\n"
         "class Post(models.Model):\n"
         "    title = models.CharField(max_length=200)\n\n"
         "    class Meta:\n"
         "        permissions = [\n"
         "            ('publish_post', 'Can publish post'),\n"
         "        ]"
     )},

    {"chapter_slug": "file-uploads", "order": 1, "section_type": "theory", "heading": "Handling Uploads Safely",
     "content": (
         "File uploads need validation and storage planning. During development, uploaded files can live in "
         "MEDIA_ROOT. In production, use durable storage such as S3, Cloudinary, or another object store.\n\n"
         "Important checks:\n"
         "- Limit file size.\n"
         "- Validate file extension and content type.\n"
         "- Store files outside source code.\n"
         "- Never trust uploaded file names.\n"
         "- Serve media through a web server or object storage, not the Django dev server."
     ), "code": ""},
    {"chapter_slug": "file-uploads", "order": 2, "section_type": "code", "heading": "Image Upload Example",
     "content": "", "code": (
         "# models.py\n"
         "class Profile(models.Model):\n"
         "    avatar = models.ImageField(upload_to='avatars/%Y/%m/', blank=True)\n\n"
         "# forms.py\n"
         "class ProfileForm(forms.ModelForm):\n"
         "    class Meta:\n"
         "        model = Profile\n"
         "        fields = ['avatar']\n\n"
         "# template\n"
         "<form method=\"post\" enctype=\"multipart/form-data\">\n"
         "  {% csrf_token %}\n"
         "  {{ form.as_p }}\n"
         "  <button type=\"submit\">Upload</button>\n"
         "</form>\n\n"
         "# settings.py\n"
         "MEDIA_URL = '/media/'\n"
         "MEDIA_ROOT = BASE_DIR / 'media'"
     )},

    {"chapter_slug": "email", "order": 1, "section_type": "theory", "heading": "Email in Django",
     "content": (
         "Django can send email through SMTP or custom email backends. Email is used for password reset, "
         "account verification, notifications, invoices, and alerts.\n\n"
         "In development, use the console email backend so emails print in the terminal. In production, "
         "use a real provider and keep credentials in environment variables."
     ), "code": ""},
    {"chapter_slug": "email", "order": 2, "section_type": "code", "heading": "Email Settings and Sending",
     "content": "", "code": (
         "# settings.py development\n"
         "EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'\n\n"
         "# settings.py production example\n"
         "EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'\n"
         "EMAIL_HOST = 'smtp.example.com'\n"
         "EMAIL_PORT = 587\n"
         "EMAIL_USE_TLS = True\n"
         "EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']\n"
         "EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']\n\n"
         "# views.py\n"
         "from django.core.mail import send_mail\n\n"
         "send_mail(\n"
         "    'Welcome',\n"
         "    'Thanks for joining.',\n"
         "    'noreply@example.com',\n"
         "    ['user@example.com'],\n"
         ")"
     )},

    {"chapter_slug": "pagination-search", "order": 1, "section_type": "theory", "heading": "Large Lists Need Controls",
     "content": (
         "Real apps should not render thousands of rows at once. Pagination keeps pages fast. Search and "
         "filtering help users find records quickly.\n\n"
         "Common patterns:\n"
         "- paginate_by on ListView.\n"
         "- Paginator for function-based views.\n"
         "- GET parameters for search and filters.\n"
         "- PostgreSQL full-text search for advanced search.\n"
         "- django-filter for reusable filtering forms."
     ), "code": ""},
    {"chapter_slug": "pagination-search", "order": 2, "section_type": "code", "heading": "Search with Pagination",
     "content": "", "code": (
         "from django.core.paginator import Paginator\n"
         "from django.db.models import Q\n"
         "from django.shortcuts import render\n\n"
         "def post_list(request):\n"
         "    q = request.GET.get('q', '')\n"
         "    posts = Post.objects.all()\n"
         "    if q:\n"
         "        posts = posts.filter(Q(title__icontains=q) | Q(body__icontains=q))\n\n"
         "    paginator = Paginator(posts, 10)\n"
         "    page_obj = paginator.get_page(request.GET.get('page'))\n"
         "    return render(request, 'blog/post_list.html', {'page_obj': page_obj, 'q': q})"
     )},

    {"chapter_slug": "management-commands", "order": 1, "section_type": "theory", "heading": "Custom manage.py Commands",
     "content": (
         "Management commands let you create project-specific command line tools. Use them for imports, "
         "cleanup jobs, reports, one-time maintenance, and scheduled tasks.\n\n"
         "Location pattern:\n"
         "app_name/management/commands/command_name.py\n\n"
         "Then run it with python manage.py command_name."
     ), "code": ""},
    {"chapter_slug": "management-commands", "order": 2, "section_type": "code", "heading": "Custom Command Example",
     "content": "", "code": (
         "# blog/management/commands/publish_old_drafts.py\n"
         "from django.core.management.base import BaseCommand\n"
         "from blog.models import Post\n\n"
         "class Command(BaseCommand):\n"
         "    help = 'Publish all draft posts'\n\n"
         "    def add_arguments(self, parser):\n"
         "        parser.add_argument('--dry-run', action='store_true')\n\n"
         "    def handle(self, *args, **options):\n"
         "        drafts = Post.objects.filter(status='draft')\n"
         "        if options['dry_run']:\n"
         "            self.stdout.write(f'{drafts.count()} posts would be published')\n"
         "            return\n"
         "        updated = drafts.update(status='published')\n"
         "        self.stdout.write(self.style.SUCCESS(f'Published {updated} posts'))"
     )},

    {"chapter_slug": "transactions", "order": 1, "section_type": "theory", "heading": "Keeping Data Consistent",
     "content": (
         "Transactions group database operations so they either all succeed or all roll back. They matter for "
         "payments, inventory, account balances, subscriptions, and workflows that update multiple tables.\n\n"
         "Use transaction.atomic() around operations that must stay consistent. Use select_for_update() when "
         "two requests might update the same row at the same time."
     ), "code": ""},
    {"chapter_slug": "transactions", "order": 2, "section_type": "code", "heading": "Atomic Transaction Example",
     "content": "", "code": (
         "from django.db import transaction\n\n"
         "@transaction.atomic\n"
         "def transfer_money(from_account, to_account, amount):\n"
         "    from_account.balance -= amount\n"
         "    to_account.balance += amount\n"
         "    from_account.save(update_fields=['balance'])\n"
         "    to_account.save(update_fields=['balance'])\n\n"
         "@transaction.atomic\n"
         "def reserve_product(product_id):\n"
         "    product = Product.objects.select_for_update().get(pk=product_id)\n"
         "    if product.stock <= 0:\n"
         "        raise ValueError('Out of stock')\n"
         "    product.stock -= 1\n"
         "    product.save(update_fields=['stock'])"
     )},

    {"chapter_slug": "advanced-admin", "order": 1, "section_type": "theory", "heading": "Admin Beyond Registration",
     "content": (
         "The Django admin can become a powerful internal tool. You can customize list pages, filters, "
         "fieldsets, readonly fields, inlines, permissions, bulk actions, and query performance.\n\n"
         "Use it for trusted staff workflows, not as a public-facing product UI."
     ), "code": ""},
    {"chapter_slug": "advanced-admin", "order": 2, "section_type": "code", "heading": "Admin Optimization",
     "content": "", "code": (
         "@admin.register(Post)\n"
         "class PostAdmin(admin.ModelAdmin):\n"
         "    list_display = ['title', 'author', 'status', 'created_at']\n"
         "    list_select_related = ['author', 'category']\n"
         "    list_filter = ['status', 'created_at']\n"
         "    search_fields = ['title', 'body']\n"
         "    readonly_fields = ['created_at', 'updated_at']\n"
         "    actions = ['mark_published']\n\n"
         "    def mark_published(self, request, queryset):\n"
         "        updated = queryset.update(status='published')\n"
         "        self.message_user(request, f'{updated} posts published')\n\n"
         "    def has_delete_permission(self, request, obj=None):\n"
         "        return request.user.is_superuser"
     )},

    {"chapter_slug": "cbv-deep", "order": 1, "section_type": "theory", "heading": "How CBVs Think",
     "content": (
         "Class-based views organize request handling into methods. The request enters dispatch(), which chooses "
         "get(), post(), put(), or another method. Generic views add reusable behavior through mixins.\n\n"
         "Important methods:\n"
         "- get_queryset(): choose objects.\n"
         "- get_context_data(): add template context.\n"
         "- get_object(): fetch one object.\n"
         "- form_valid(): handle valid form submission.\n"
         "- get_success_url(): choose redirect target."
     ), "code": ""},
    {"chapter_slug": "cbv-deep", "order": 2, "section_type": "code", "heading": "CBV Method Overrides",
     "content": "", "code": (
         "class PostListView(ListView):\n"
         "    model = Post\n"
         "    paginate_by = 10\n\n"
         "    def get_queryset(self):\n"
         "        return Post.objects.filter(status='published').select_related('author')\n\n"
         "    def get_context_data(self, **kwargs):\n"
         "        context = super().get_context_data(**kwargs)\n"
         "        context['featured_posts'] = Post.objects.filter(featured=True)[:3]\n"
         "        return context\n\n"
         "class PostCreateView(LoginRequiredMixin, CreateView):\n"
         "    model = Post\n"
         "    fields = ['title', 'body']\n\n"
         "    def form_valid(self, form):\n"
         "        form.instance.author = self.request.user\n"
         "        return super().form_valid(form)"
     )},

    {"chapter_slug": "drf-advanced", "order": 1, "section_type": "theory", "heading": "DRF Production Features",
     "content": (
         "Django REST Framework becomes powerful when you add permissions, authentication, pagination, filtering, "
         "throttling, versioning, nested serializers, and clear error handling.\n\n"
         "Common production needs:\n"
         "- Token/JWT/session authentication.\n"
         "- Per-view permissions.\n"
         "- Search, ordering, and filtering.\n"
         "- Pagination for list endpoints.\n"
         "- Throttling to reduce abuse.\n"
         "- Serializer validation and nested writes."
     ), "code": ""},
    {"chapter_slug": "drf-advanced", "order": 2, "section_type": "code", "heading": "Advanced DRF ViewSet",
     "content": "", "code": (
         "from rest_framework import viewsets, permissions, filters\n"
         "from rest_framework.pagination import PageNumberPagination\n\n"
         "class StandardPagination(PageNumberPagination):\n"
         "    page_size = 20\n\n"
         "class PostViewSet(viewsets.ModelViewSet):\n"
         "    serializer_class = PostSerializer\n"
         "    permission_classes = [permissions.IsAuthenticatedOrReadOnly]\n"
         "    pagination_class = StandardPagination\n"
         "    filter_backends = [filters.SearchFilter, filters.OrderingFilter]\n"
         "    search_fields = ['title', 'body']\n"
         "    ordering_fields = ['created_at', 'title']\n\n"
         "    def get_queryset(self):\n"
         "        return Post.objects.select_related('author').filter(status='published')\n\n"
         "    def perform_create(self, serializer):\n"
         "        serializer.save(author=self.request.user)"
     )},

    {"chapter_slug": "channels", "order": 1, "section_type": "theory", "heading": "Real-Time Django",
     "content": (
         "Django Channels adds WebSocket support for real-time features like chat, notifications, live dashboards, "
         "presence, collaborative editing, and streaming status updates.\n\n"
         "Channels uses ASGI instead of only WSGI. For production, Redis is commonly used as the channel layer."
     ), "code": ""},
    {"chapter_slug": "channels", "order": 2, "section_type": "code", "heading": "Basic WebSocket Consumer",
     "content": "", "code": (
         "# chat/consumers.py\n"
         "import json\n"
         "from channels.generic.websocket import AsyncWebsocketConsumer\n\n"
         "class ChatConsumer(AsyncWebsocketConsumer):\n"
         "    async def connect(self):\n"
         "        self.room_group_name = 'chat_global'\n"
         "        await self.channel_layer.group_add(self.room_group_name, self.channel_name)\n"
         "        await self.accept()\n\n"
         "    async def disconnect(self, close_code):\n"
         "        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)\n\n"
         "    async def receive(self, text_data):\n"
         "        data = json.loads(text_data)\n"
         "        await self.channel_layer.group_send(\n"
         "            self.room_group_name,\n"
         "            {'type': 'chat_message', 'message': data['message']},\n"
         "        )\n\n"
         "    async def chat_message(self, event):\n"
         "        await self.send(text_data=json.dumps({'message': event['message']}))"
     )},

    {"chapter_slug": "celery", "order": 1, "section_type": "theory", "heading": "Background Jobs",
     "content": (
         "Some work should not happen inside a web request: sending emails, generating reports, resizing images, "
         "syncing APIs, charging subscriptions, and scheduled cleanup. Celery runs these tasks in worker processes.\n\n"
         "Celery usually needs a broker such as Redis or RabbitMQ. For scheduled tasks, use Celery Beat."
     ), "code": ""},
    {"chapter_slug": "celery", "order": 2, "section_type": "code", "heading": "Celery Task Example",
     "content": "", "code": (
         "# config/celery.py\n"
         "import os\n"
         "from celery import Celery\n\n"
         "os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')\n"
         "app = Celery('config')\n"
         "app.config_from_object('django.conf:settings', namespace='CELERY')\n"
         "app.autodiscover_tasks()\n\n"
         "# blog/tasks.py\n"
         "from celery import shared_task\n"
         "from django.core.mail import send_mail\n\n"
         "@shared_task\n"
         "def send_welcome_email(email):\n"
         "    send_mail('Welcome', 'Thanks for joining.', 'noreply@example.com', [email])"
     )},

    {"chapter_slug": "docker", "order": 1, "section_type": "theory", "heading": "Why Docker Helps",
     "content": (
         "Docker packages the app and its runtime dependencies so development and deployment environments are "
         "more consistent. For Django, Docker is commonly paired with PostgreSQL, Redis, Celery, and Nginx.\n\n"
         "Use Docker to make onboarding easier and production closer to local development."
     ), "code": ""},
    {"chapter_slug": "docker", "order": 2, "section_type": "code", "heading": "Simple Dockerfile",
     "content": "", "code": (
         "FROM python:3.12-slim\n\n"
         "ENV PYTHONDONTWRITEBYTECODE=1\n"
         "ENV PYTHONUNBUFFERED=1\n\n"
         "WORKDIR /app\n"
         "COPY requirements.txt .\n"
         "RUN pip install --no-cache-dir -r requirements.txt\n"
         "COPY . .\n\n"
         "CMD [\"gunicorn\", \"config.wsgi:application\", \"--bind\", \"0.0.0.0:8000\"]"
     )},

    {"chapter_slug": "cicd", "order": 1, "section_type": "theory", "heading": "Automating Quality",
     "content": (
         "CI/CD runs checks automatically when code is pushed. For Django projects, start with installing "
         "dependencies, running migrations checks, running tests, and optionally deploying after success.\n\n"
         "Good pipelines catch mistakes before LinkedIn visitors, teammates, or users see them."
     ), "code": ""},
    {"chapter_slug": "cicd", "order": 2, "section_type": "code", "heading": "GitHub Actions Test Workflow",
     "content": "", "code": (
         "name: tests\n\n"
         "on: [push, pull_request]\n\n"
         "jobs:\n"
         "  test:\n"
         "    runs-on: ubuntu-latest\n"
         "    steps:\n"
         "      - uses: actions/checkout@v4\n"
         "      - uses: actions/setup-python@v5\n"
         "        with:\n"
         "          python-version: '3.12'\n"
         "      - run: pip install -r requirements.txt\n"
         "      - run: python manage.py test\n"
         "      - run: python manage.py check --deploy"
     )},

    {"chapter_slug": "logging-monitoring", "order": 1, "section_type": "theory", "heading": "Seeing Production Problems",
     "content": (
         "Production apps need visibility. Logging records what happened. Monitoring shows whether the app is "
         "healthy. Error tracking captures exceptions with stack traces and context.\n\n"
         "Track:\n"
         "- request errors and status codes.\n"
         "- slow queries and slow views.\n"
         "- failed background jobs.\n"
         "- failed logins or suspicious behavior.\n"
         "- uptime and response time."
     ), "code": ""},
    {"chapter_slug": "logging-monitoring", "order": 2, "section_type": "code", "heading": "Basic Logging Config",
     "content": "", "code": (
         "LOGGING = {\n"
         "    'version': 1,\n"
         "    'disable_existing_loggers': False,\n"
         "    'handlers': {\n"
         "        'console': {'class': 'logging.StreamHandler'},\n"
         "    },\n"
         "    'loggers': {\n"
         "        'django': {\n"
         "            'handlers': ['console'],\n"
         "            'level': 'INFO',\n"
         "        },\n"
         "        'myapp': {\n"
         "            'handlers': ['console'],\n"
         "            'level': 'DEBUG',\n"
         "            'propagate': False,\n"
         "        },\n"
         "    },\n"
         "}"
     )},

    {"chapter_slug": "postgres", "order": 1, "section_type": "theory", "heading": "Why PostgreSQL Is Popular with Django",
     "content": (
         "SQLite is excellent for learning, but PostgreSQL is a common production choice. Django supports many "
         "PostgreSQL features such as indexes, constraints, JSON fields, full-text search, and advanced lookups.\n\n"
         "Use PostgreSQL when you need stronger concurrency, production reliability, advanced search, and "
         "database-level constraints."
     ), "code": ""},
    {"chapter_slug": "postgres", "order": 2, "section_type": "code", "heading": "Indexes and Constraints",
     "content": "", "code": (
         "from django.db import models\n"
         "from django.db.models import Q\n\n"
         "class Post(models.Model):\n"
         "    title = models.CharField(max_length=200)\n"
         "    slug = models.SlugField()\n"
         "    status = models.CharField(max_length=20)\n"
         "    metadata = models.JSONField(default=dict, blank=True)\n\n"
         "    class Meta:\n"
         "        indexes = [\n"
         "            models.Index(fields=['status', '-id']),\n"
         "        ]\n"
         "        constraints = [\n"
         "            models.UniqueConstraint(fields=['slug'], name='unique_post_slug'),\n"
         "            models.CheckConstraint(check=Q(status__in=['draft', 'published']), name='valid_status'),\n"
         "        ]"
     )},

    {"chapter_slug": "multidb", "order": 1, "section_type": "theory", "heading": "Using More Than One Database",
     "content": (
         "Most projects need one database. Advanced systems may use multiple databases for legacy data, analytics, "
         "read replicas, multi-tenant separation, or gradual migrations.\n\n"
         "Django supports named databases and database routers. Keep this simple unless the project truly needs it."
     ), "code": ""},
    {"chapter_slug": "multidb", "order": 2, "section_type": "code", "heading": "Multiple Database Settings",
     "content": "", "code": (
         "DATABASES = {\n"
         "    'default': {\n"
         "        'ENGINE': 'django.db.backends.postgresql',\n"
         "        'NAME': 'app',\n"
         "    },\n"
         "    'analytics': {\n"
         "        'ENGINE': 'django.db.backends.postgresql',\n"
         "        'NAME': 'analytics',\n"
         "    },\n"
         "}\n\n"
         "# query a specific database\n"
         "Report.objects.using('analytics').all()\n\n"
         "# save to a specific database\n"
         "report.save(using='analytics')"
     )},

    {"chapter_slug": "internals", "order": 1, "section_type": "theory", "heading": "How Django Starts",
     "content": (
         "Understanding internals helps when debugging confusing behavior. On startup, Django loads settings, "
         "configures installed apps, imports app configs, prepares models, then serves requests through the "
         "URL resolver and middleware stack.\n\n"
         "Key internals:\n"
         "- manage.py sets DJANGO_SETTINGS_MODULE.\n"
         "- django.setup() initializes the app registry.\n"
         "- URLResolver matches paths to views.\n"
         "- Middleware wraps the view call.\n"
         "- Template loaders find templates.\n"
         "- ORM query compilers turn QuerySets into SQL."
     ), "code": ""},
    {"chapter_slug": "internals", "order": 2, "section_type": "code", "heading": "Manual Django Setup",
     "content": "", "code": (
         "import os\n"
         "import django\n\n"
         "os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')\n"
         "django.setup()\n\n"
         "from blog.models import Post\n"
         "print(Post.objects.count())\n\n"
         "# Useful in standalone scripts, but management commands are usually better."
     )},
])

COMMANDS.update({
    ("email", "Email & Password Reset Commands"): [
        ("python -m smtpd -n -c DebuggingServer localhost:1025", "Run a local debug SMTP server on older Python versions"),
    ],
    ("management-commands", "Management Command Commands"): [
        ("python manage.py help", "List available management commands"),
        ("python manage.py help command_name", "Show help for one command"),
        ("python manage.py publish_old_drafts --dry-run", "Run a custom command without changing data"),
    ],
    ("channels", "Channels Commands"): [
        ("pip install channels channels-redis", "Install Django Channels and Redis channel layer support"),
        ("uvicorn config.asgi:application", "Run the ASGI application"),
    ],
    ("celery", "Celery Commands"): [
        ("pip install celery redis", "Install Celery and Redis client"),
        ("celery -A config worker -l info", "Start a Celery worker"),
        ("celery -A config beat -l info", "Start Celery Beat for scheduled tasks"),
    ],
    ("docker", "Docker Commands"): [
        ("docker build -t django-app .", "Build the Django Docker image"),
        ("docker run -p 8000:8000 django-app", "Run the Django container"),
        ("docker compose up --build", "Start a multi-service Docker setup"),
    ],
    ("cicd", "CI/CD Commands"): [
        ("python manage.py test", "Run tests locally before pushing"),
        ("python manage.py check", "Run Django system checks"),
        ("python manage.py check --deploy", "Run deployment checks in CI"),
    ],
})


def seed(apps, schema_editor):
    Chapter = apps.get_model('learn', 'Chapter')
    Section = apps.get_model('learn', 'Section')
    Command = apps.get_model('learn', 'Command')

    # Clear existing data
    Command.objects.all().delete()
    Section.objects.all().delete()
    Chapter.objects.all().delete()

    # Create chapters
    chapter_map = {}
    for data in CHAPTERS:
        ch = Chapter.objects.create(**data)
        chapter_map[data['slug']] = ch

    # Create sections and build lookup for commands
    section_map = {}
    for data in SECTIONS:
        ch = chapter_map[data.pop('chapter_slug')]
        sec = Section.objects.create(chapter=ch, **data)
        section_map[(ch.slug, sec.heading)] = sec

    # Create commands
    for (ch_slug, sec_heading), cmds in COMMANDS.items():
        sec = section_map[(ch_slug, sec_heading)]
        for i, (cmd, desc) in enumerate(cmds, start=1):
            Command.objects.create(section=sec, order=i, cmd=cmd, description=desc)


def unseed(apps, schema_editor):
    Command = apps.get_model('learn', 'Command')
    Section = apps.get_model('learn', 'Section')
    Chapter = apps.get_model('learn', 'Chapter')
    Command.objects.all().delete()
    Section.objects.all().delete()
    Chapter.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed, unseed),
    ]
