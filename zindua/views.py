from django.shortcuts import render

def index(request):
    context = {
        'school_name': 'Zindua School',
        'tagline': 'Empowering Africa through Tech Education',
        'stats': [
            {'label': 'Students', 'value': '2000+'},
            {'label': 'Programmes', 'value': '10+'},
            {'label': 'Instructors', 'value': '50+'},
            {'label': 'Alumni', 'value': '5000+'},
        ]
    }
    return render(request, 'index.html', context)

def about(request):
    context = {
        'mission': 'To bridge the tech skills gap in Africa.',
        'founded': 2017,
        'team': [
            {'name': 'Alice Kamau', 'role': 'CEO'},
            {'name': 'Brian Otieno', 'role': 'CTO'},
            {'name': 'Clara Mwangi', 'role': 'Head of Curriculum'},
        ]
    }
    return render(request, 'about.html', context)

def contact(request):
    context = {
        'email': 'info@zinduaschool.com',
        'phone': '+254 700 000 000',
        'location': 'Nairobi, Kenya',
        'socials': ['Twitter', 'LinkedIn', 'Instagram']
    }
    return render(request, 'contact.html', context)

def programmes(request):
    context = {
        'programmes': [
            {
                'name': 'Software Engineering',
                'duration': '6 months',
                'level': 'Beginner to Advanced',
                'description': 'Full stack web development using modern technologies.',
                'skills': ['Python', 'JavaScript', 'React', 'Django']
            },
            {
                'name': 'Data Science',
                'duration': '4 months',
                'level': 'Intermediate',
                'description': 'Data analysis, ML and AI fundamentals.',
                'skills': ['Python', 'Pandas', 'Matplotlib', 'Scikit-learn']
            },
            {
                'name': 'Cybersecurity',
                'duration': '3 months',
                'level': 'Beginner',
                'description': 'Network security, ethical hacking and defense.',
                'skills': ['Linux', 'Networking', 'Kali', 'Firewalls']
            },
            {
                'name': 'Mobile Development',
                'duration': '5 months',
                'level': 'Intermediate',
                'description': 'Build cross-platform mobile apps.',
                'skills': ['React Native', 'Flutter', 'Firebase']
            },
        ]
    }
    return render(request, 'programmes.html', context)