<!-- Main Headline Here... -->
<h1 align='center'> 🍕 Pizza Restaurant Management System - tkinter GUI </h1>

<div align="center">
    <img src="https://github.com/Trigenaris/pizza-restaurant-management-system/blob/main/crazy_logo.png">
</div>

In this project; we focus on a **Restaurant Management**, specifically a made-up restaurant called *Crazy Pizza Restaurant*. The restaurant management system has a menu stored in a database that contains *CRUD* operations and has a system in which any item can be ordered. Also, orders are part of the database structure to analyze the current situation of the restaurant. The main features of the system are as shown with the help of the referred modules and libraries:

## 📌 Required Modules:
* sqlite3
* tkinter
* datetime
* pandas
* matplotlib
* functools (for the decorator)
* winsound (for the custom message boxes)

#### ❓ Abbreviations: 
* **EF:** Some of the features that are signed as **EF** means **extra features** which can be excluded in the final version of the project.
* **WIP:** Headlines signed as **WIP** means **work in progress** which are not fully completed yet.

<hr>

## 📌 Main Features:
* **login system** for the user to see the related menu on their screen.
* 3 main menus refer to roles respectively: **Manager, Waiter, Chef**
* It is planned that the system will have **custom message boxes** other than default ones in the tkinter. (WIP) (EF)
* Different roles have **different functionalities** to do that are **responsive** to each other.

### 👩‍💼 Features of the Manager:
* Editing the menu (**Adding, updating or removing products**)
* Checking the current, canceled, or completed orders.
* Checking, and analyzing daily, weekly, monthly, or yearly reports.

### 🤵‍♀️ Features of the Waiter: 
* Checking the Menu.
* Taking orders.
* Cancelling orders.
* Pinging **the taken orders** to the chef.

### 👩‍🍳 Features of the Chef:
* Checking the Menu.
* Checking the taken orders.
* Pinging **the prepared orders** to the waiter.

<hr>

<h2>
    How Does It Work?
</h2>

The application starts with a login screen that expects the user to log in from one of the three roles:

* 1️⃣ First the user chooses the role
* 2️⃣ Then enters the password (Only for the manager)
* 3️⃣ Lastly, clicks the login button

![pizza1](https://github.com/Trigenaris/pizza-restaurant-management-system/assets/122381599/a102a1ec-e0a3-4403-bc36-7da03b6d0972)

# Manager Menu

After logging in, the related menu appears on the screen. (Manager menu for example)

## Show Menu

* There are four different tabs for different functionalities in the manager menu.
* 1️⃣ As the user clicks `Show Menu` button, 2️⃣ whole products appear on the right frame.

![pizza2](https://github.com/Trigenaris/pizza-restaurant-management-system/assets/122381599/2cab8763-fd0c-4f45-b803-0b8bab81bd5c)

## New Product

* 1️⃣ The user clicks the `New Product` button,
* 2️⃣ A new window appears to be filled in,
* 3️⃣ The user clicks the `Add Product` button to add the product to the menu and the database:

![pizza3](https://github.com/Trigenaris/pizza-restaurant-management-system/assets/122381599/acc82845-ee91-4a67-b339-b83f3b981c0f)
![pizza4](https://github.com/Trigenaris/pizza-restaurant-management-system/assets/122381599/e6125be6-74e8-4c82-acdd-d04866f4015b)
![pizza5](https://github.com/Trigenaris/pizza-restaurant-management-system/assets/122381599/f63bbd66-1a57-419c-9a5d-31cd49e00404)

## Remove Product

* 1️⃣ The user selects a product from the menu,
* 2️⃣ Clicks `Remove Product` button,
* 3️⃣ The application asks again to the user to be sure about the process,
* 4️⃣ The selected product is deleted from the menu and the database!

![pizza6](https://github.com/Trigenaris/pizza-restaurant-management-system/assets/122381599/2a5dc2ad-ca7d-4d31-83e6-5013e2445147)
![pizza7](https://github.com/Trigenaris/pizza-restaurant-management-system/assets/122381599/eddbe8ca-944f-418f-a36b-6583d53ddd96)

## Update Product

* 1️⃣ The user selects a product from the menu,
* 2️⃣ Clicks the `Update Product` button,
* 3️⃣ Enters new information about the product,
* 4️⃣ Clicks the `Update Product` button in the new window,
* 5️⃣ The application asks again to the user to be sure about the process,
* 6️⃣ The selected product is updated in the menu and the database!

![pizza8](https://github.com/Trigenaris/pizza-restaurant-management-system/assets/122381599/1932840f-ae27-44a1-8648-88729fe1c227)
![pizza9](https://github.com/Trigenaris/pizza-restaurant-management-system/assets/122381599/dc6ad490-0744-4a3d-b0ed-eaa70ba832be)

<hr>

# Waiter Menu

When the user logs in as the **waiter**, another window appears with the same layout but different buttons and tabs.

The waiter can check the menu whenever he/she chooses **the product type** from the left frame:

![pizza10](https://github.com/Trigenaris/pizza-restaurant-management-system/assets/122381599/ab2fae54-f4b7-4070-a781-8671fbf91d8f)

## Take Order

* 1️⃣ Firstly, the user chooses **the product type**.
* 2️⃣ Then, chooses **product name**.
* 3️⃣ After that, chooses **the quantity** of the current product.
* 4️⃣ Lastly, the user clicks `Add to Order` button to see the total order and the total price.

![pizza11](https://github.com/Trigenaris/pizza-restaurant-management-system/assets/122381599/84725f14-0eda-4196-831e-8a4c7b9e6eba)

* 5️⃣ When the order is ready to complete, the user clicks `Complete Order` button.
* 6️⃣ Then, the user chooses customer type,
* 7️⃣ And writes down the customer information.
* 8️⃣Finally the user clicks `Submit Order` button to add the order in **the active orders** tab and the database.

![pizza12](https://github.com/Trigenaris/pizza-restaurant-management-system/assets/122381599/4ff303c8-e425-4f11-ac0a-9fb2d9801ba3)

## Active Orders

Whenever the user clicks `Show Active Orders` button in the **Active Orders** tab, he/she can see the details of the orders which are currently active.

![pizza13](https://github.com/Trigenaris/pizza-restaurant-management-system/assets/122381599/1f4b5e34-f2b9-4dd1-b225-867aeb07779e)

<hr>

# Chef Menu

Like the waiter, chef also can check the whole menu;

![pizza14](https://github.com/Trigenaris/pizza-restaurant-management-system/assets/122381599/21536f35-7a4d-4590-8775-e9f85fbb8fe5)

## Preparing Order

Chef's specific function in the menu is finishing active orders.

* 1️⃣ Firstly, the user selects one of the active orders,
* 2️⃣ Then clicks `Order Ready` button,
* 3️⃣ And an information window appears as the message says that the order is transferred from the active order to finished order. (Both in GUI and in the database)

![pizza15](https://github.com/Trigenaris/pizza-restaurant-management-system/assets/122381599/98810c8f-7136-4a7f-9fa2-c21c366944ee)

## Finished Orders

* 1️⃣ The user clicks `Finished Orders` tab.
* 2️⃣ Then clicks `Show Finished Orders` button.
* 3️⃣ And the finished orders appears on the right frame with their details. (Prepared hour is also added to the finished orders.)

<hr>

# Manager Menu (Analysis)

Let's get back to the manager menu for the analysis feature:

Oops! Looks like the user entered an invalid password!

![pizza17](https://github.com/Trigenaris/pizza-restaurant-management-system/assets/122381599/4c36af06-ab38-4d8b-9fdd-83af927cf06f)

## Analysis

The related graph appears on the right frame as the user selects the anaylsis type and clicks `Show Analysis` button:

![pizza18](https://github.com/Trigenaris/pizza-restaurant-management-system/assets/122381599/ea4fb325-6624-45c8-a57d-76c6998177e2)
![pizza19](https://github.com/Trigenaris/pizza-restaurant-management-system/assets/122381599/2731ee05-3375-4ee6-bcf6-5ddc568c39af)

<hr>

The project will have notices as it progresses in the future.

<hr>
