from django.shortcuts import render, get_object_or_404, redirect
from .models import PropertyListing
from .forms import PropertyListingForm, PropertyListingSearchForm

# View to create a new property listing
def listing_create(request):
    if request.method == 'POST':  # Check if the form is submitted
        form = PropertyListingForm(request.POST, request.FILES)  # Create form with POST data and files
        if form.is_valid():  # Validate form data
            form.save()  # Save the new listing to the database
            return redirect('listings:listings_list')  # Redirect to the listings list after saving
    else:
        form = PropertyListingForm()  # Create an empty form
    return render(request, 'listings/listing_form.html', {'form': form})  # Render the form template

# View to display all property listings
def listing_list(request):
    listings = PropertyListing.objects.all()  # Retrieve all listings from the database
    return render(request, 'listings/listing_list.html', {'listings': listings})  # Render the listings template

# View to filter listings by status
def listing_filter(request, sale_status):
    listings = PropertyListing.objects.filter(status=sale_status)
    return render(request, 'listings/listing_list.html', {'listings': listings})




# View to update an existing property listing
def listing_update(request, pk):
    listing = get_object_or_404(PropertyListing, pk=pk)  # Get the listing by primary key or return 404

    if request.method == 'POST':  # Check if the form is submitted
        form = PropertyListingForm(request.POST, request.FILES, instance=listing)  # Create form with POST data and files, bound to the existing listing

        if form.is_valid():  # Validate form data
            form.save()  # Save the updated listing to the database
            return redirect('listings:listings_list')  # Redirect to the listings list after saving

    else:
        form = PropertyListingForm(instance=listing)  # Create a form pre-filled with the existing listing data
    return render(request, 'listings/listing_form.html', {'form': form})  # Render the form template

# View to delete a property listing
def listing_delete(request, pk):
    listing = get_object_or_404(PropertyListing, pk=pk)  # Get the listing by primary key or return 404
    if request.method == 'POST':  # Check if the form is submitted to confirm deletion
        listing.delete()  # Delete the listing from the database
        return redirect('listings:listings_list')  # Redirect to the listings list after deletion
    return render(request, 'listings/listing_confirm_delete.html', {'listing': listing})  # Render the delete confirmation template

# View to display detailed information for a single property listing
def listing_detail(request, pk):
    listing = get_object_or_404(PropertyListing, pk=pk)  # Get the listing by primary key or return 404
    return render(request, 'listings/listing_detail.html', {'listing': listing})  # Render the detail template


def property_search(request):
    form = PropertyListingSearchForm(request.GET or None)
    properties = PropertyListing.objects.all()

    if form.is_valid():
        keyword = form.cleaned_data.get('keyword')
        location = form.cleaned_data.get('location')
        property_type = form.cleaned_data.get('property_type')
        min_price = form.cleaned_data.get('min_price')
        max_price = form.cleaned_data.get('max_price')
        num_bedrooms= form.cleaned_data.get('bedrooms')
        num_bathrooms = form.cleaned_data.get('bathrooms')

        if keyword:
            properties = properties.filter(title__icontains=keyword)
        if location:
            properties = properties.filter(location__icontains=location)
        if property_type:
            properties = properties.filter(property_type=property_type)
        if min_price is not None:
            properties = properties.filter(price__gte=min_price)
        if max_price is not None:
            properties = properties.filter(price__lte=max_price)
        if num_bedrooms is not None:
            properties = properties.filter(bedrooms__gte=num_bedrooms)
        if num_bathrooms is not None:
            properties = properties.filter(bathrooms__gte=num_bathrooms)

    context = {
        'form': form,
        'properties': properties,
    }
    return render(request, 'listings/property_search.html', context)
