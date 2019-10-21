Release notes
#############

Release notes for **Shopit**.

----

0.5.2
=====

* Fix setup requirement.

0.5.1
=====

* Drop `Django 1.10` support.
* In `ProductDetailView`, check for renderer format before adding django-cms menu related items.
* Remove `PhoneNumberField` from the project, use simple `CharField` instead.
* Lock requirements.

0.5.0
=====

* Rename package from `djangoshop-shopit` to `django-shopit`.

0.4.3
=====

* Fix encoding error in product admin `get_name` method.
* Add `phonenumbers` library to requirements.

0.4.2
=====

* Fixes #7 - "unhashable type: 'MoneyInEUR'" error in `get_price_steps` templatetag.

0.4.1
=====

* Small fixes in admin.
* Fix indentation in admin help text for ``djangocms-admin-style``.
* Refactor tests.

0.4.0
=====

* Add support for *Django 1.11* & *DjangoSHOP 0.12.x*.
* Handle tousand separator when displaying money in admin.
* Add ability to pass in ``order_number`` to ``order`` templatetag.
* Add ``num_uses`` to list display for Discount Code.
* After order was populated with cart data, delete discount codes.
* Add ability to send `validate` key when updating the cart via POST. In which
  case the promo code gets validated without applying it to cart.
* Add setting ``SHOPIT_DEFAULT_PRODUCT_ORDER`` to control default ordering of products.
* Add ability to override ``ProductSerializer`` fields through the ``fields`` GET property.
* Add ``attribute_choices`` to product serializer fields.
* Add ``template`` field to Flag model, adn a ``SHOPIT_FLAG_TEMPLATES`` setting.
* Add ``path`` to the Flag serializer.
* Include categorization flags on a product.
* Fix flag serializer field.
* Use attachment ``subject_location`` when generating a thumbnail.
* Add ability to pass in ``get_count`` as boolean through the ``request.GET`` object when in
  ``ProductListView`` and ``CategoryDetailView``. This applies in non HTML formated response and returns the count of
  all (filtered) products as ``{'count': 300}``.
* Simplify urls into a single ``urls.py`` since https://github.com/divio/django-cms/pull/5898 was merged.
* Separate admin modules into multiple files.
* Move settings from ``settings.py`` to ``conf.py`` and re-format based on *djangoSHOP's* settings pattern.
* Add ``SHOPIT_ASYNC_PRODUCT_LIST`` and ``SHOPIT_ADD_PRODUCT_LIST_TO_CONTEXT`` settings to optimize ``ProductListView``
  and ``CategoryDetailView``.
* Bump ``django-cms`` requirement to 3.5.
* Set default prices to zero.
* Fix field indentation in models and forms to follow Django's style guide.
* Various bugfixes.

.. attention::

  Requires ``python manage.py migrate shopit`` to set default price and amount Money fields, and add a template
  field to the Flag model.

0.3.0
=====

* Handle ``InvalidImageFormatError`` error when generating thumbnails.
* Add support for djangoSHOP 0.11.

0.2.3
=====

* Add ``never_cache`` decorators to account, review and watch views.
* Optimize ``get_flags`` templatetag when filtering by products.
* Add ``content`` field as ``PlaceholderField`` to categorization models.
* Force setting priority on address form, order existant addresses by priority.
* Update ``query_transform`` templatetag to remove empty values.
* Add missing ``FlagModelForm`` to ``FlagAdmin``.
* Fix Flag unicode error in ``__str__``.
* Re-work the reviews, making them non-translatable. Not compatible with the old reviews, make sure to save them
  (if you have any) before upgrading. A way for adding reviews was not provided before so this should not be the case.
* Add setting ``SHOPIT_REVIEW_ACTIVE_DEFAULT``. This decides if created reviews are active by default.
* Handle updating shopping cart via ajax, add success messages to it.
* Remove *CartDiscountCode's* from cart when emptying it, make last applied code appears as active.
* Add *PhoneNumberField* field to the customer, add setting ``SHOPIT_PHONE_NUMBER_REQUIRED`` that defaults to ``False``.
* Refactor address forms, enable using either 'shipping' or 'billing' form as primary. added setting ``SHOPIT_PRIMARY_ADDRESS``.
* Fix address country choices.
* Add and track num uses on a *DiscountCode*, alter the admin to display new values.
* Enable frontend editing of categorization and product models.
* Fix *AccountOrderDetail* view not returning the correct order.
* Handle NoReverseMatch for ``add_to_cart_url`` in a Product serializer.

.. attention::

  Requires ``python manage.py migrate shopit`` to add/remove fields on a Review model,
  as well as add ``phone_number`` field on Customer model, ``content`` field on Categorization models
  and ``max_uses``, ``num_uses`` on *DiscountCode*.

.. note::

  If migrating with categorization models already added. You'll need to save each models again for the
  ``content`` PlaceholderField to appear.

0.2.2
=====

* Add filtering by modifiers.
* Update django-shop requirement to 0.10.2.

0.2.1
=====

* Fixes problem with migrations.

0.2.0
=====

* Add support for *Django 1.10* & *DjangoSHOP 0.10.x*.
* Alter templates to use Bootstrap 4 by default.
* Create example project, move tests.
* Rename description & caption fields to start with underscore.

.. attention::

    Requires ``python manage.py migrate shopit`` to add a product code to the CartItem, rename description & caption
    fields, as well as adding an additional setting
    ``SHOP_PRODUCT_SUMMARY_SERIALIZER = 'shopit.serializers.ProductSummarySerializer'``.

0.1.4
=====

* Add *description* field to categorization models.
* Move variant generator methods from admin to the model. Now ``create_all_variants`` and ``create_variant`` are
  available on the model.
* Update add to cart ``get_context`` to ensure correct product translation is returned.

.. attention::

  Requires ``python manage.py migrate shopit`` to create description field on categorization models.

0.1.3
=====

* Bugfixes.
* Fix ``get_object`` and ``get_queryset`` in product views returning inconsistant results.
* Add ``get_view_url`` to product detail view to return correct translated url.

0.1.2
=====

* Add price range filtering in ``get_products`` templatetag.
* Move product filtering to a manager.
* Allow mutiple flags to be passed to the ``get_products`` templatetag.
* Optimize attribute filtering with *prefetch_related*.
* Enable sorting the products.
* Don't fetch flags from categorization on a product. Categorization flags are used separately to mark categorization
  and the don't affect the products.
* Fix templatetags.
* Add option to limit ``get_categorization`` templatetag to a set of products.
* Enable filtering categorization and flags via querystring. Change price range querystrings.
* Add ``get_flags`` templatetag.
* Make *Flag* model an mptt model with a parent field.
* Show flags as filter_horizontal instead of CheckboxInput in product admin.
* Show localized amounts in product admin summary field.
* Use ``as_decimal`` when displaying price steps in template instead of floatformat.

.. attention::

  Requires ``python manage.py migrate shopit`` to create mptt fields on a Flag model.

0.1.1
=====

* Ensure customer is recognized before registering a new account. This works around an error
  **"Unable to proceed as guest without items in the cart"** when registering without a cart.
* Make fields in product serializer editable through settings, set optimized defaults.
* Fix error when mergin dictionaries in python3.
* Remove redundant code.
* Fix trying to generate image thumbnail on attachment when *file* is None.
* Fix weight setter setting width instead of weight.

0.1.0
=====

* Initial release.
