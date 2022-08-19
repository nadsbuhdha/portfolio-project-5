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