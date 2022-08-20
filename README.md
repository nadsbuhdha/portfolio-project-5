# Sole Society 

Sole Society is an ecommerce website focusing on sneakers.

Sole Society provides users will the ability to purchase exclusive sneakers. Authenticated users can utilise the review and favourite features whilst store owners can access the CRUD functionality by adding editing publishing and deleting products to sell. 

A live version of the site is available [here](https://sole-society.herokuapp.com/)

## Table Of Contents 
** add 

## UX 


### Strategy 

The purpose of this website was to provide users with an ecommerce store where they can purcahse sneakers. Agile methodologies were utilised in order to create the website. 

#### Project Goals

### User Stories 

### Epic 1 - Site Foundations 

* As a site user I can click navigation links so that I can navigate throughout the site
* As a site user I can receive messages for the actions performed on the website so that I am constantly aware of the actions I have performed
* As a site user I can click on social media links, including the facebook page, so that I can follow the stores social media presence
* As a site user I can sign up for a newsletter so that I am aware of the latest store news / products

### Epic 2 - Products

* As a site user I can see an overview of the product details whilst in list view so that I am aware of the product details before clicking on the product

* As a site user I can view individual product details so that I can see more in depth details of products

* As a site user I can sort products by rating, gender or brand so that I can filter products to easily find a product I am searching for

* As a site user I can select the size of the product so that I can purchase the correct size

* As a site user I can select the quantity of the product ** so that I can purchase the correct quantity.

### Epic 3 - The bag 

* As a site user I can see an overview of the products I have in my bag so that I am aware of what products I am about to purchase

* As a site user I can I can to easily add items to my bag so that I can add extra products I would like to purchase before completing payment.

* As a site user I can see the price of my bag so that I am aware of the cost of my purchases

* As a site user I can I can add or delete items from my bag so that I can remove or change any items I do not want before checking out

* As a site user I can alter the size and quantity of the product so that I have the correct size and quantity before purchase.

### Epic 4 - The checkout 

* As a site user I can see an overview of my bag so that I can confirm I am happy with purchases before payment

* As a site user I can  enter my payment details** so that I can purchase my items with relative ease.

* As a guest user I can enter my details without having to sign in** so that I can still make a purchase as a guest
*  As a logged in user my details are automatically entered so that I can avoid repetitive actions

* As a site user I can I am informed whether my purchase has gone through so that I know whether the purchase has been successful

### Epic 5 - Account registration 

* As a user I can sign up to become a registered account user so that I can access the sites registered users functions

* As a registered user I can store my details so that I do not have to continually enter my details such as shipping

* As a registered user I can save items till later so that I can return later to purchase or remove items

* As a registered user I can view my order history so that I can see what items I have previous purchased

### Epic 6 - Reviews

* As a site user I can read reviews so that I can see what other users feel about purchased products

* As a registered user I can write reviews for products so that I can share my opinion on the products purchased

* As a registered user I can delete a review so that  it can be removed if I no longer want it to be displayed

### Epic 7 - Store Owner 

* As a store owner I can add a product so that I can sell my product online

* As a store owner I can ** edit a product so that I can edit product details

* As a store owner I can I can delete a product so that I can remove the product from sales


### Strategy Table 

In order to create a site which is relevant to its target auidence, various other related website were researched first in order to comprehensively analyse the features which would be necessary.

| Feature        | Importance  | Viability  |
| ------------- |:-------------:| -----:|
| Responsive design | 5 | 5 |
| Product List View     | 5 | 5 |
| Product Detail View      | 5 | 5 |
| Product Sort     | 5 | 5 |
| Product Search     | 5 | 5 |
| Shopping Bag Overview     | 5 | 5 |
| Bag update notifcation      | 4 | 4 |
| Alter quantities of product in bag      | 4 | 4 |
| Order Summary in checkout     | 5 | 4 |
| Display purcahse total    | 5 | 5 |
| Payment system      | 5 | 5 |
| Feedback that order is complete     | 5 | 5 |
| View Reviews      | 3 | 3 |
| Write & Delete reviews      | 3 | 3 |
| User Registration     | 5 | 5 |
| Favourite Products      | 3 | 4 |
| User Newsletter subscription   | 4 | 4 |
| Create, Update, Delete products for superuser      | 5 | 5 |
| Reccomended products for registered user      | 1 | 1 |

### Scope

The project was developed in mulitple phases in order to build a minimum viable product. This product could then be developed and extended on. 

### Phase 1 

* Responsive design
* Product List View
* Product Detail View
* Product Sort
* Product Search
* Shopping Bag Overview
* Bag update notifcation
* Payment system
* Alter quantities of product in bag
* Order Summary in checkout
* Display purcahse total 
* Feedback that order is complete
* User Registration
* Create, Update, Delete products for superuser



### Phase 2 
* View Reviews 
* Write & Delete reviews
* Favourite Products
* User Newsletter subscription


### Phase 3 
*  Reccomended products for registered user

## User Stories
Throughout the project, Github project board was used as a management tool to track user stories. 
This allowed the project to focus on particular specific tasks whilst being built. 

**** ADD USER STORY IMAGES

## Structure 

It is imperative that users can naviagate through the site easily and instinctively. In order to adhere to this the following considerations undertaken:

(Add structure image ?)

* Responsive design throughout the site. 
* Header, footer and navagation visable and consistant throughout entire site. 
* Clearly labelled links.
* Consistant font sizing and colouring throughout site. 


## Database Model

Planned Database Model: 
![Database](document_assets/images/sole_model.jpeg)

Final Database Model:
(insert database screenshots)

## Design 

### Wireframes

Before building the site, Balsamiq was utilised to create wireframes of the site. Wireframes were created in order to develop the websites aesthetic and to give an impression of the responsive style across different platforms.

| Page        | Desktop  | Mobile version  |
| ------------- |:-------------:| -----:|
| Home Page | ![Desktop Home](document_assets/images/desktop_home.png)|![Mobile Home](document_assets/images/mobile_home.png)|
| All Products | ![Desktop all Products](document_assets/images/desktop_all_products.png)  | ![Mobile all Products](document_assets/images/mobile_all_products.png)  |
| Product Details | ![desktop product detail](document_assets/images/desktop_product_detail.png)|  ![mobile product detail](document_assets/images/mobile_product_detail.png)|
| Shopping Bag | ![desktop shopping bag](document_assets/images/desktop_shopping_bag.png) | ![mobile shopping bag](document_assets/images/mobile_shopping_bag.png) |
| Checkout |![desktop checkout](document_assets/images/desktop_checkout.png) | ![mobile checkout](document_assets/images/mobile_checkout.png) |
| Order Summary | ![desktop order summary](document_assets/images/desktop_ordersummary.png) | ![mobile order summary](document_assets/images/mobile_ordersummary.png) | 
| Sign In | ![desktop sign in](ddocument_assets/images/desktop_sign_in.png) | ![mobile sign in](document_assets/images/mobile_sign_in.png) |
| Sign Up | ![desktop sign up](document_assets/images/desktop_sign_up.png)  | ![mobile sign up](document_assets/images/mobile_sign_up.png)|
|Sign Out | ![desktop sign out](document_assets/images/desktop_sign_out.png) | ![mobile sign out](document_assets/images/mobile_sign_out.png)|
| User Profile | ![desktop user profile](document_assets/images/desktop_profile.png) | ![mobile user profile](document_assets/images/mobile_profile.png) |
|Adding Products as superuser | ![desktop add product](document_assets/images/desktop_add_product.png)|  ![mobile add product](document_assets/images/mobile_add_product.png) |
| Editing Products as superuser|![desktop edit product](document_assets/images/desktop_edit_product.png)|![mobile edit product](document_assets/images/mobile_edit_product.png)|
| Admin Products View| ![desktop product management view](document_assets/images/desktop_product_management.png) | ![mobile product management view](document_assets/images/mobile_product_management.png) |


### Colour Schemes

During the design phase of building the site, various sneaker focuesed ecommerece stores were researched. Colours are used sparingly so I decided to adopt this neutral approach aesthetically. 

#FFFFFF white was used for the majority of the background and header. 
#212529  was used for buttons and product cards.
#080808 was used for the footer

### Fonts 

Nunito was used as the primary font across the site. After research into ecommerece fonts, Nunito was chosen for its well-balanced appearance and rounded asaesthetic, which compliments the rounded border radius which features across the site. San-serif was chosen as a backup font, should Nunito fail. 

## Marketing

ADD MARKETING SECTION


## Features 

* The entire website has been designed with a responsive mobile first approach.

The Header of the site features the site logo which links back to the homepage. The navigation links allow the shopper to navagate and access differening sections across the website.
![header](document_assets/images/ss_header.png)

The header features a dropdown menu where users can navagate to products filtered by the specific category they pick. 
![drop down menu](document_assets/images/dropdownmenu.png)

When a user send an item to the bag, the bag on the header highlights and displays current bag price.
![highlighted bag](document_assets/images/highlighted_bag.png)

Users can search for specific products with the use of the searchbar. 
![search bar](document_assets/images/searchbar.png)

The homepage features a carousel of product images. The carousel features a button where users can navagate to all products.
![carousel](document_assets/images/caroulsel.png)

The footer features on each page. Social media icons feautre on the footer, including the facebook page. Users can also sign up to the newsletter. 
![footer](document_assets/images/footer.png)

### Products Page 

The products page features all of the stores products in individual cards. Products can be filtered by Mens, Womens, Accessories & special offers. Products can be futher filtered by best sellers, exlusives, new arrivals, sport shoes and essentials. 
Products can also be sorted by price, rating, name, category and brand. 
![products page](document_assets/images/products_page.png)

The product card features the name of the product, the brand, the price,  rating for the product and the ability to favourite a product. 
![products page](document_assets/images/product_card.png)


### Product detail

The product detail page features The name of the product, a larger version of the product image, the the product brand, the price, the product rating and a short description of the product.
Users can favourite the product from here. 
User can select the size and quantity of the product from this page. 
Once size and quantity users can either add the product to the bag or continue to shop. 
Users can view reviews of the product and authenticated users can leave a review of a product. 
![products detail](document_assets/images/product_detail.png)


Reviews

### Bag page

If a user clicks on the bag page and there are no products in the bag then an empty bag message is displayed 
![empty bag](document_assets/images/empty_bag.png)


When a user has products in their bag, the product image, name, sku, price and quantity are displayed. Users can update the quantity of a product from the shopping bag. Users can also remove a product from the bag. The grand total, including the delivery fee (if there is one) is, also featured towards the bottom of the page. The proceed to checkout button or continue shopping buttons are also present. 
![shopping bag](document_assets/images/shopping_bag.png)



### Checkout Page

The checkout page features an overview of the products the user is intending to purcahse. 
A form is present for the user to fill out in order to complete the purchase.
Included in the form is a section for users to input their card details. This is connected to stripe payments system. 
Under the payment form, a message is displayed informing the shopper the amount to be charged on the provided card.
Adjust bag and complete order buttons are featured so users can edit their order or complete their order
![checkout page](document_assets/images/checkout_page.png)

### Checkout Success 

![payment success](document_assets/images/payment_success.png)

The payment success page shows a summary of the users order, with an order number.
Users are notified of an email that will be sent to confirm their order. 


The payment system has been connected to a webhook to ensure payments succeed and products are sent. 
![payment success](document_assets/images/webhook_succeeded.png)


### My Profile 

User profile page features a form for users to store default delivery information as well as their order history. 
User profile also features the products the users has favourited. 
![My Profile](document_assets/images/my_profile.png)


### Account Pages 

| Page        | Feature  | Image  |
| ------------- |:-------------:| -----:|
| Sign In | The sign in page allows users to sign in with their account details |![Sign In](document_assets/images/sign_in.png)|
| Sign Out | Users can sign out from this page|![Sign Out](document_assets/images/sign_out.png)|
| Sign Up | Unregistered users can sign up to the website here |![Sign Up](document_assets/images/sign_up.png)|


### Product Management

| Page        | Feature  | Image  |
| ------------- |:-------------:| -----:|
| Add Products | This page allows users to add new products using the form |![Add Product](document_assets/images/add_product.png)|
| Edit Products | This page allows users to edit products using the form with the previously entered data |![Edit Product](document_assets/images/edit_product.png)|
| Delete Products | From the products page, superusers can delete products|![Delete Product](document_assets/images/delete_product.png)|


### Review 

Signed in users can leave reviews on specific products. Users can also decide to delete their reviews.
![Reviews](document_assets/images/reviews.png)

Users can only leave one review per product. 
![one](document_assets/images/one_review.png)

### 404 Page

** add image **
A custom 404 page is utilised. Users can click the 'return home' button to return to the home page.

## Technologies Used

### Languages 
* HTML5
* CSS3
* JavaScript
* Python

### Libraries and Frameworks
* Django - web framework.

* Bootstrap 5 -  used for the styling and responsiveness of the site. 

* Google Fonts - used for fonts across the site

* Font - Awesome  used across the website to add icons.

* jQuery - used to simplify HTML and DOM manipulation.

### Packages 

* Django Allauth 

* Django Crispy Forms

* Django Countries

* Pillow.

* Gunicorn.


### Database 

* SQLite.

* Heroku Postgres database.


### Tools, storage & services

* Amazon Web Service - used to store static files and media.

* Stripe - Used to handle and process online payment.

* GitPod

* Github

* Heroku - Deployed site was hosted.

* W3C Markup and Jigsaw validation - used to test and validate the HTML and CSS.

* PEP8 - for validating the python code.

* JSHINT - for validating the javasctipy code.

