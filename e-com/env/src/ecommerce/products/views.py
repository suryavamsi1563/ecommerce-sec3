from django.shortcuts import render,get_object_or_404
from django.http import Http404
# Create your views here.
from django.views.generic import DetailView
from django.views.generic import ListView
from .models import Product

class ProductfeaturedListView(ListView):
    # queryset = Product.objects.all()
    template_name = 'products/product_list.html'

    def get_queryset(self,*args,**kwargs):
        request = self.request
        return Product.objects.all().featured()

class ProductfeaturedDetailView(DetailView):
    # queryset = Product.objects.all()
    template_name = 'products/featured-detail.html'

    def get_queryset(self,*args,**kwargs):
        request = self.request
        return Product.objects.featured()

class ProductListView(ListView):
    # queryset = Product.objects.all()
    template_name = 'products/product_list.html'

    def get_queryset(self,*args,**kwargs):
        request = self.request
        return Product.objects.all()

    # def get_context_data(self,*args,**kwargs):
    #     context = super(ProductListView,self).get_context_data(*args,**kwargs)
    #     print(context)
    #     return context

class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = 'products/detail.html'

    def get_object(self,*args,**kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        # instance = get_object_or_404(Product,slug=slug)
        try:
            instance = Product.objects.get(slug=slug)
        except Product.DoesNotExist:
            raise Http404("Not found..")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug)
            instance =  qs.first()
        except:
            raise Http404("Yjjjjjjjjj")
        return instance

class ProductDetailView(DetailView):
    # queryset = Product.objects.all()
    template_name = 'products/detail.html'

    def get_context_data(self,*args,**kwargs):
        context = super(ProductDetailView,self).get_context_data(*args,**kwargs)
        print(context)
        return context

    def get_object(self,*args,**kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Product doesn't exist")
        return instance

    # def get_queryset(self,*args,**kwargs):
    #     request = self.request
    #     pk = self.kwargs.get('pk')
    #     return Product.objects.filter(pk = pk)