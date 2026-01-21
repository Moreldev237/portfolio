from django.shortcuts import render
from django.conf import settings

def home(request):
    technologies = {
        'Développement Web': [
            {'name': 'HTML', 'icon': 'devicon-html5-plain'},
            {'name': 'CSS', 'icon': 'devicon-css3-plain'},
            {'name': 'JavaScript', 'icon': 'devicon-javascript-plain'},
            {'name': 'Bootstrap', 'icon': 'devicon-bootstrap-plain'},
            {'name': 'Tailwind CSS', 'icon': 'devicon-tailwindcss-plain'},
            {'name': 'Python', 'icon': 'devicon-python-plain'},
            {'name': 'Django', 'icon': 'devicon-django-plain'},
            {'name': 'FastAPI', 'icon': 'devicon-fastapi-plain'},
            {'name': 'Flask', 'icon': 'devicon-flask-original'},
        ],
        'DevOps': [
            {'name': 'Linux', 'icon': 'devicon-linux-plain'},
            {'name': 'Docker', 'icon': 'devicon-docker-plain'},
            {'name': 'Ansible', 'icon': 'devicon-ansible-plain'},
            {'name': 'Kubernetes', 'icon': 'devicon-kubernetes-plain'},
            {'name': 'Terraform', 'icon': 'devicon-terraform-plain'},
            {'name': 'GitHub Actions', 'icon': 'devicon-githubactions-plain'},
            {'name': 'Prometheus', 'icon': 'devicon-prometheus-original'},
            {'name': 'Grafana', 'icon': 'devicon-grafana-original'},
            {'name': 'SonarQube', 'icon': 'devicon-sonarqube-original'},
            {'name': 'Traefik', 'icon': 'devicon-traefikproxy-plain'},
        ],
        'Cloud': [
            {'name': 'AWS', 'icon': 'devicon-amazonwebservices-plain'},
            {'name': 'GCP', 'icon': 'devicon-googlecloud-plain'},
            {'name': 'Azure', 'icon': 'devicon-azure-plain'},
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
            'image': 'projects/ecommerce.jpg',
            'demo_url': 'https://demo-ecommerce.example.com',
            'source_url': 'https://github.com/username/ecommerce',
        },
        {
            'title': 'Dashboard DevOps',
            'description': 'Dashboard de monitoring avec métriques en temps réel.',
            'skills': ['FastAPI', 'Grafana', 'Prometheus', 'Docker'],
            'image': 'projects/devops-dashboard.jpg',
            'demo_url': 'https://dashboard.example.com',
            'source_url': 'https://github.com/username/devops-dashboard',
        },
        {
            'title': 'API REST Microservices',
            'description': 'Architecture microservices avec orchestration Kubernetes.',
            'skills': ['FastAPI', 'Kubernetes', 'Docker', 'PostgreSQL'],
            'image': 'projects/microservices.jpg',
            'demo_url': 'https://api.example.com',
            'source_url': 'https://github.com/username/microservices-api',
        },
        {
            'title': 'Portfolio Personnel',
            'description': 'Site portfolio responsive avec animations modernes.',
            'skills': ['Django', 'Tailwind CSS', 'JavaScript', 'GSAP'],
            'image': 'projects/portfolio.jpg',
            'demo_url': '#',
            'source_url': 'https://github.com/username/portfolio',
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
            'title': 'AWS Certified Solutions Architect',
            'issuer': 'Amazon Web Services',
            'date': '2023',
            'credential_id': 'AWS-123456',
            'icon': 'devicon-amazonwebservices-plain colored',
            'verify_url': 'https://aws.amazon.com/verification',
        },
        {
            'title': 'Docker Certified Associate',
            'issuer': 'Docker Inc.',
            'date': '2023',
            'credential_id': 'DCA-789012',
            'icon': 'devicon-docker-plain colored',
            'verify_url': 'https://docker.com/certification',
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
    context = {
        'social_links': settings.SOCIAL_LINKS,
    }
    return render(request, 'main/contact.html', context)