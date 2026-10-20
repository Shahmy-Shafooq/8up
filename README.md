# 8up

8up is a campus hub that helps students, discover local food, buy from student sellers, and split bills with friends.


## Tech Stack

- **Backend:** Python (Flask)
- **Database:** SQLite
- **Frontend:** HTML, CSS, JavaScript

## Features

### Campus Marketplace Module
- **Accounts** – sign up, login, logout, change password, show/hide password, choose Consumer or Seller
- **Seller storefronts** – create, edit and delete business profile with operating hours, delivery zones and social links
- **Listings** – add, edit, delete products and update stock
- **Listing details** – images, price, description and seller contact
- **Categories, search and filter** – by category, faculty, food type and price
- **Homepage** – featured sellers and daily specials
- **Favourites** – save and remove favourite sellers or listings
- **Reviews and ratings** – rate sellers and leave written reviews

### Smart Utility & Food Discovery Module
- **U-Split** – split group bills including tax and service charges
- **Food discovery** – short video reviews, trending dishes, local food guides

### Governance Module
- **Reporting** – students can report inappropriate listings
- **Admin** – review reports, manage users, remove inappropriate content

## Team and Work Division

### Thureyya – User Accounts & Business Profiles
- Develop dual-role user registration and login with secure password hashing.
- Implement user profile management.
- Create seller storefronts with business descriptions, operating hours, delivery zones, and contact links.
- Develop product categories and filtering by faculty, food type, and delivery options.
- Implement the favourites feature for businesses and advertisements.

### Shahmy – Product Management & Governance
- Develop product listing features, including creating, editing, and deleting advertisements.
- Implement stock availability toggles and product image uploads.
- Develop keyword search and sorting by price and recency.
- Develop the admin dashboard for reviewing flagged listings and managing user accounts.
- Implement platform activity monitoring.

### Sofia – Food Discovery, Smart Utilities & Homepage
- Create the U-Split Bill Calculator with itemized bill splitting and proportional tax/service charges.
- Implement QR-code sharing for bill summaries.
- Develop the homepage business discovery feed featuring active sellers, daily specials, and featured vendors.
- Create the TikTok-style food discovery feed with food reviews and student seller clips.
- Implement the Trending Dishes section and engagement counters.
- Integrate all modules and assist with system testing and debugging.

### Shared Responsibilities
- Collaborate on SQLite database design and integration.
- Maintain consistent HTML, CSS, and Flask coding standards.
- Test and debug the complete application.
- Contribute to documentation and the final presentation.

## Getting Started

1. Clone the repository:
   ```bash
   git clone <repository-link>
   cd 8up
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate        # Windows
   source venv/bin/activate     # macOS / Linux
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:
   ```bash
   python app.py
   ```

5. Open `http://127.0.0.1:5000` in your browser.


## Team Workflow

- Each member works on their own branch 
- Open a Pull Request to merge into `main` when a feature is done.
- Run `git pull` on `main` before starting new work.
