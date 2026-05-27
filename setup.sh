#!/bin/bash
set -e

echo "=============================="
echo "  Django Learn — Setup"
echo "=============================="

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

python manage.py migrate
python manage.py migrate --run-syncdb

echo ""
echo "=============================="
echo "  Done! Now run:"
echo "  source venv/bin/activate"
echo "  python manage.py runserver"
echo "  Open: http://localhost:8000"
echo ""
echo "  Admin panel: http://localhost:8000/admin/"
echo "  Run: python manage.py createsuperuser"
echo "=============================="
