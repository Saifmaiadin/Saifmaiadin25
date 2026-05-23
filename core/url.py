# core/urls.py (أضف إلى router)
from customers.views import CustomerViewSet
from products.views import ProductViewSet, ServiceViewSet

router.register(r'customers', CustomerViewSet)
router.register(r'products', ProductViewSet)
router.register(r'services', ServiceViewSet)