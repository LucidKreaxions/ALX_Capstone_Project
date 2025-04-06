from django.contrib import admin
from .models import Category, Product, Order


# Category Admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)  # Search by category
    prepolutated_fields = {'slug': ('name',)}  # Auto - fill slug based on name
    ordering = ('name',)  # Alphabetical


# Product Admin
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'stock_quantity', 'created_at')
    search_fields = ('name', 'category__name')  # Search by product & category
    list_filter = ('category', 'price', 'stock_quantity')  # Filters in the sidebar
    ordering = ('-created_at',)  # Show newest products first
    prepopulated_fields = {'slug': ('name',)}  # Auto-generate slugs
    list_editable = ('price', 'stock_quantity')  # Allow quick editing in the list view
    readonly_fields = ('created_at',)  # Make created_at non-editable
    fieldsets = (  # Organizing form fields
        ('Basic Information', {'fields': ('name', 'slug', 'description', 'category', 'price')}),
        ('Stock & Media', {'fields': ('stock_quantity', 'image')}),
        ('Metadata', {'fields': ('created_at',)}),
    )


# Order Admin
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'quantity', 'total_price', 'status', 'created_at')
    list_filter = ('status', 'created_at')  # Filter by order status
    search_fields = ('user__username', 'product__name')  # Search by user or product
    ordering = ('-created_at',)  # Show latest orders first
    readonly_fields = ('total_price', 'created_at')  # Ensure total_price isn't manually edited
    fieldsets = (
        ('Customer & Product Details', {'fields': ('user', 'product', 'quantity')}),
        ('Order Status & Pricing', {'fields': ('status', 'total_price')}),
        ('Timestamps', {'fields': ('created_at',)}),
    )


# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
