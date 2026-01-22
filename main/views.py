from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from django.http import JsonResponse
import json

def home(request):
    technologies = {
        'Développement Web': [
            {'name': 'HTML', 'icon': 'devicon-html5-plain colored'},
            {'name': 'CSS', 'icon': 'devicon-css3-plain colored'},
            {'name': 'JavaScript', 'icon': 'devicon-javascript-plain colored'},
            {'name': 'Bootstrap', 'icon': 'devicon-bootstrap-plain colored'},
            {'name': 'Tailwind CSS', 'icon': 'devicon-tailwindcss-plain colored'},
            {'name': 'Python', 'icon': 'devicon-python-plain colored'},
            {'name': 'Django', 'icon': 'devicon-django-plain colored'},
            {'name': 'FastAPI', 'icon': 'devicon-fastapi-plain colored'},
            {'name': 'Flask', 'icon': 'devicon-flask-original colored'},
        ],
        'DevOps': [
            {'name': 'Linux', 'icon': 'devicon-linux-plain colored'},
            {'name': 'Docker', 'icon': 'devicon-docker-plain colored'},
            {'name': 'Ansible', 'icon': 'devicon-ansible-plain colored'},
            {'name': 'Kubernetes', 'icon': 'devicon-kubernetes-plain colored'},
            {'name': 'Terraform', 'icon': 'devicon-terraform-plain colored'},
            {'name': 'GitHub Actions', 'icon': 'devicon-githubactions-plain colored'},
            {'name': 'Prometheus', 'icon': 'devicon-prometheus-original colored'},
            {'name': 'Grafana', 'icon': 'devicon-grafana-original colored'},
            {'name': 'SonarQube', 'icon': 'devicon-sonarqube-original colored'},
            {'name': 'Traefik', 'icon': 'devicon-traefikproxy-plain colored'},
        ],
        'Cloud': [
            {'name': 'AWS', 'icon': 'devicon-amazonwebservices-plain colored'},
            {'name': 'GCP', 'icon': 'devicon-googlecloud-plain colored'},
            {'name': 'Azure', 'icon': 'devicon-azure-plain colored'},
        ]
    }
    
    context = {
        'technologies': technologies,
        'social_links': settings.SOCIAL_LINKS,
    }
    return render(request, 'main/home.html', context)

def projects(request):
    projects_data = [
        {
            'title': 'Application E-commerce',
            'description': 'Plateforme e-commerce complète avec paiement en ligne et gestion des stocks.',
            'skills': ['Django', 'PostgreSQL', 'Stripe API', 'Docker'],
            'image': 'images/projects/ecommerce.jpg',
            'demo_url': 'https://demo-ecommerce.example.com',
            'source_url': 'https://github.com/username/ecommerce',
        },
        {
            'title': 'Dashboard DevOps',
            'description': 'Dashboard de monitoring avec métriques en temps réel.',
            'skills': ['FastAPI', 'Grafana', 'Prometheus', 'Docker'],
            'image': 'images/projects/devops-dashboard.jpg',
            'demo_url': 'https://dashboard.example.com',
            'source_url': 'https://github.com/username/devops-dashboard',
        },
        {
            'title': 'API REST Microservices',
            'description': 'Architecture microservices avec orchestration Kubernetes.',
            'skills': ['FastAPI', 'Kubernetes', 'Docker', 'PostgreSQL'],
            'image': 'images/projects/microservices.jpg',
            'demo_url': 'https://api.example.com',
            'source_url': 'https://github.com/username/microservices-api',
        },
        {
            'title': 'Portfolio Personnel',
            'description': 'Site portfolio responsive avec animations modernes.',
            'skills': ['Django', 'Tailwind CSS', 'JavaScript', 'GSAP'],
            'image': 'images/projects/portfolio.jpg',
            'demo_url': '#',
            'source_url': 'https://github.com/Moreldev237/portfolio.git',
        },
    ]
    
    context = {
        'projects': projects_data,
        'social_links': settings.SOCIAL_LINKS,
    }
    return render(request, 'main/projects.html', context)

def certifications(request):
    certifications_data = [
        {
            'title': 'Linux Fundamentals',
            'issuer': 'LearnQuest',
            'date': 'Decembre 2025',
            'credential_id': 'CN55BW3L00NK',
            'icon': 'devicon-LearnQuest-plain colored',
            'verify_url': 'https://www.coursera.org/account/accomplishments/records/CN55BW3L00NK',
        },
        {
            'title': 'Introduction to containers with Docker/Kubernetes/OpenShift',
            'issuer': 'IBM',
            'date': 'Decembre 2025',
            'credential_id': 'XVA6FW2NTFUQ',
            'icon': 'devicon-docker-plain colored',
            'verify_url': 'https://www.coursera.org/account/accomplishments/records/XVA6FW2NTFUQ',
        },
        {
            'title': 'Python Django Developer',
            'issuer': 'Meta',
            'date': '2022',
            'credential_id': 'META-345678',
            'icon': 'devicon-django-plain',
            'verify_url': 'https://coursera.org/verify/ABCD1234',
        },
        {
            'title': 'Kubernetes Administrator',
            'issuer': 'Linux Foundation',
            'date': '2022',
            'credential_id': 'CKA-901234',
            'icon': 'devicon-kubernetes-plain colored',
            'verify_url': 'https://training.linuxfoundation.org',
        },
    ]
    
    context = {
        'certifications': certifications_data,
        'social_links': settings.SOCIAL_LINKS,
    }
    return render(request, 'main/certifications.html', context)

def contact(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            email = data.get('email')
            subject = data.get('subject')
            message = data.get('message')
            
            # Validate required fields
            if not all([name, email, subject, message]):
                return JsonResponse({'success': False, 'message': 'Tous les champs sont requis.'}, status=400)
            
            # Prepare email
            email_subject = f"Portfolio Contact: {subject}"
            email_message = f"""
Nouveau message depuis le portfolio :

De: {name} ({email})

Sujet: {subject}

Message:
{message}
"""
            
            # Send email
            send_mail(
                email_subject,
                email_message,
                settings.EMAIL_HOST_USER,  # From
                [settings.EMAIL_HOST_USER],  # To (yourself)
                fail_silently=False,
            )
            
            return JsonResponse({'success': True, 'message': 'Message envoyé avec succès !'})
            
        except Exception as e:
            return JsonResponse({'success': False, 'message': f'Erreur lors de l\'envoi: {str(e)}'}, status=500)
    
    context = {
        'social_links': settings.SOCIAL_LINKS,
    }
    return render(request, 'main/contact.html', context)