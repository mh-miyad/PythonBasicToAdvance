#!/usr/bin/env python3
"""
Direct File Creator - A simple script to create HTML and CSS files without using VS Code controller.
"""

import os
import sys
import argparse

def create_price_page(output_path):
    """Create a price page with Bootstrap styling"""
    print(f"Creating price page at {output_path}")
    
    # Create HTML file
    html_path = os.path.join(output_path, "price.html")
    css_path = os.path.join(output_path, "price.css")
    
    # Create HTML content
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Pricing Plans</title>
  <!-- Bootstrap CSS -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <!-- Custom CSS -->
  <link rel="stylesheet" href="price.css">
</head>
<body>
  <div class="container py-5">
    <header class="text-center mb-5">
      <h1 class="display-4 fw-bold">Pricing Plans</h1>
      <p class="lead text-muted">Choose the perfect plan for your needs</p>
    </header>
    
    <div class="row row-cols-1 row-cols-md-3 mb-3 text-center">
      <!-- Basic Plan -->
      <div class="col">
        <div class="card mb-4 rounded-3 shadow-sm">
          <div class="card-header py-3">
            <h4 class="my-0 fw-normal">Basic</h4>
          </div>
          <div class="card-body">
            <h1 class="card-title pricing-card-title">$9<small class="text-muted fw-light">/mo</small></h1>
            <ul class="list-unstyled mt-3 mb-4">
              <li>10 users included</li>
              <li>2 GB of storage</li>
              <li>Email support</li>
              <li>Help center access</li>
            </ul>
            <button type="button" class="w-100 btn btn-lg btn-outline-primary">Sign up for free</button>
          </div>
        </div>
      </div>
      
      <!-- Pro Plan -->
      <div class="col">
        <div class="card mb-4 rounded-3 shadow-sm border-primary">
          <div class="card-header py-3 text-white bg-primary border-primary">
            <h4 class="my-0 fw-normal">Pro</h4>
          </div>
          <div class="card-body">
            <h1 class="card-title pricing-card-title">$29<small class="text-muted fw-light">/mo</small></h1>
            <ul class="list-unstyled mt-3 mb-4">
              <li>20 users included</li>
              <li>10 GB of storage</li>
              <li>Priority email support</li>
              <li>Help center access</li>
            </ul>
            <button type="button" class="w-100 btn btn-lg btn-primary">Get started</button>
          </div>
        </div>
      </div>
      
      <!-- Enterprise Plan -->
      <div class="col">
        <div class="card mb-4 rounded-3 shadow-sm">
          <div class="card-header py-3">
            <h4 class="my-0 fw-normal">Enterprise</h4>
          </div>
          <div class="card-body">
            <h1 class="card-title pricing-card-title">$99<small class="text-muted fw-light">/mo</small></h1>
            <ul class="list-unstyled mt-3 mb-4">
              <li>50 users included</li>
              <li>30 GB of storage</li>
              <li>Phone and email support</li>
              <li>Help center access</li>
            </ul>
            <button type="button" class="w-100 btn btn-lg btn-outline-primary">Contact us</button>
          </div>
        </div>
      </div>
    </div>
    
    <div class="row mt-5">
      <div class="col-12">
        <div class="card">
          <div class="card-header">
            <h4>Compare Plans</h4>
          </div>
          <div class="card-body">
            <div class="table-responsive">
              <table class="table table-hover">
                <thead>
                  <tr>
                    <th style="width: 34%;">Features</th>
                    <th style="width: 22%;">Basic</th>
                    <th style="width: 22%;">Pro</th>
                    <th style="width: 22%;">Enterprise</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Users</td>
                    <td>10</td>
                    <td>20</td>
                    <td>50</td>
                  </tr>
                  <tr>
                    <td>Storage</td>
                    <td>2 GB</td>
                    <td>10 GB</td>
                    <td>30 GB</td>
                  </tr>
                  <tr>
                    <td>Projects</td>
                    <td>3</td>
                    <td>10</td>
                    <td>Unlimited</td>
                  </tr>
                  <tr>
                    <td>Support</td>
                    <td>Email</td>
                    <td>Priority Email</td>
                    <td>Phone & Email</td>
                  </tr>
                  <tr>
                    <td>API Access</td>
                    <td><i class="fas fa-times text-danger"></i></td>
                    <td><i class="fas fa-check text-success"></i></td>
                    <td><i class="fas fa-check text-success"></i></td>
                  </tr>
                  <tr>
                    <td>Custom Domain</td>
                    <td><i class="fas fa-times text-danger"></i></td>
                    <td><i class="fas fa-check text-success"></i></td>
                    <td><i class="fas fa-check text-success"></i></td>
                  </tr>
                  <tr>
                    <td>Analytics</td>
                    <td>Basic</td>
                    <td>Advanced</td>
                    <td>Premium</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
    
    <div class="row mt-5">
      <div class="col-md-6 offset-md-3 text-center">
        <h3>Frequently Asked Questions</h3>
        <div class="accordion mt-4" id="pricingFAQ">
          <div class="accordion-item">
            <h2 class="accordion-header" id="headingOne">
              <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
                Can I change plans later?
              </button>
            </h2>
            <div id="collapseOne" class="accordion-collapse collapse show" aria-labelledby="headingOne" data-bs-parent="#pricingFAQ">
              <div class="accordion-body">
                Yes, you can upgrade or downgrade your plan at any time. Changes will be reflected in your next billing cycle.
              </div>
            </div>
          </div>
          <div class="accordion-item">
            <h2 class="accordion-header" id="headingTwo">
              <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
                Is there a free trial available?
              </button>
            </h2>
            <div id="collapseTwo" class="accordion-collapse collapse" aria-labelledby="headingTwo" data-bs-parent="#pricingFAQ">
              <div class="accordion-body">
                Yes, we offer a 14-day free trial for all plans. No credit card required.
              </div>
            </div>
          </div>
          <div class="accordion-item">
            <h2 class="accordion-header" id="headingThree">
              <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseThree" aria-expanded="false" aria-controls="collapseThree">
                Do you offer discounts for non-profits?
              </button>
            </h2>
            <div id="collapseThree" class="accordion-collapse collapse" aria-labelledby="headingThree" data-bs-parent="#pricingFAQ">
              <div class="accordion-body">
                Yes, we offer special pricing for non-profit organizations. Please contact our sales team for more information.
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Bootstrap JS Bundle with Popper -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
  <!-- Font Awesome -->
  <script src="https://kit.fontawesome.com/a076d05399.js" crossorigin="anonymous"></script>
</body>
</html>
"""
    
    # Create CSS content
    css_content = """/* Custom styles for pricing page */
body {
  background-color: #f8f9fa;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.pricing-card-title {
  font-size: 2.5rem;
  font-weight: 500;
}

.card {
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  overflow: hidden;
}

.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}

.btn-primary {
  background-color: #4361ee;
  border-color: #4361ee;
}

.btn-primary:hover {
  background-color: #3a56d4;
  border-color: #3a56d4;
}

.btn-outline-primary {
  color: #4361ee;
  border-color: #4361ee;
}

.btn-outline-primary:hover {
  background-color: #4361ee;
  color: white;
}

.card-header.bg-primary {
  background-color: #4361ee !important;
}

.border-primary {
  border-color: #4361ee !important;
}

.accordion-button:not(.collapsed) {
  background-color: #e7f1ff;
  color: #4361ee;
}

.accordion-button:focus {
  border-color: #4361ee;
  box-shadow: 0 0 0 0.25rem rgba(67, 97, 238, 0.25);
}

@media (max-width: 768px) {
  .pricing-card-title {
    font-size: 2rem;
  }
}
"""
    
    # Write files
    try:
        with open(html_path, 'w') as f:
            f.write(html_content)
        print(f"Created HTML file: {html_path}")
        
        with open(css_path, 'w') as f:
            f.write(css_content)
        print(f"Created CSS file: {css_path}")
        
        return True
    except Exception as e:
        print(f"Error creating files: {e}")
        return False

def create_card_layout(output_path):
    """Create a card layout page with Bootstrap styling"""
    print(f"Creating card layout at {output_path}")
    
    # Create HTML file
    html_path = os.path.join(output_path, "card_layout.html")
    css_path = os.path.join(output_path, "card_layout.css")
    
    # Create HTML content
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Figma-Inspired Card Layout</title>
  <!-- Bootstrap CSS -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <!-- Custom CSS -->
  <link rel="stylesheet" href="card_layout.css">
</head>
<body>
  <div class="container py-5">
    <div class="dashboard-header">
      <h1 class="text-center mb-4">Card Layout</h1>
      <p class="text-center text-muted">A collection of cards inspired by Figma designs</p>
    </div>
    
    <div class="row">
      <!-- Card 1 -->
      <div class="col-md-4">
        <div class="card">
          <img src="https://source.unsplash.com/random/300x200?nature" class="card-img-top" alt="Nature">
          <div class="card-body">
            <h5 class="card-title">Nature Card</h5>
            <p class="card-text">This card showcases beautiful nature photography with a clean, modern design.</p>
            <a href="#" class="btn btn-primary">Learn More</a>
          </div>
        </div>
      </div>
      
      <!-- Card 2 -->
      <div class="col-md-4">
        <div class="card">
          <img src="https://source.unsplash.com/random/300x200?technology" class="card-img-top" alt="Technology">
          <div class="card-body">
            <h5 class="card-title">Tech Card</h5>
            <p class="card-text">Explore the latest in technology with this sleek card design inspired by Figma.</p>
            <a href="#" class="btn btn-primary">Explore</a>
          </div>
        </div>
      </div>
      
      <!-- Card 3 -->
      <div class="col-md-4">
        <div class="card">
          <img src="https://source.unsplash.com/random/300x200?business" class="card-img-top" alt="Business">
          <div class="card-body">
            <h5 class="card-title">Business Card</h5>
            <p class="card-text">Professional business card design with modern aesthetics and clean typography.</p>
            <a href="#" class="btn btn-primary">Contact</a>
          </div>
        </div>
      </div>
    </div>
    
    <div class="row mt-4">
      <!-- Card 4 -->
      <div class="col-md-6">
        <div class="card">
          <div class="row g-0">
            <div class="col-md-4">
              <img src="https://source.unsplash.com/random/300x200?design" class="img-fluid rounded-start h-100" alt="Design" style="object-fit: cover;">
            </div>
            <div class="col-md-8">
              <div class="card-body">
                <h5 class="card-title">Horizontal Card</h5>
                <p class="card-text">A horizontal card layout that works well for featured content or important announcements.</p>
                <a href="#" class="btn btn-primary">Read More</a>
              </div>
            </div>
          </div>
        </div>
      </div>
      
      <!-- Card 5 -->
      <div class="col-md-6">
        <div class="card bg-dark text-white">
          <img src="https://source.unsplash.com/random/300x200?night" class="card-img" alt="Night">
          <div class="card-img-overlay" style="background: rgba(0,0,0,0.5);">
            <h5 class="card-title">Overlay Card</h5>
            <p class="card-text">This card uses an overlay effect to place text on top of an image.</p>
            <a href="#" class="btn btn-light">Discover</a>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Bootstrap JS Bundle with Popper -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
"""
    
    # Create CSS content
    css_content = """/* Custom styles for card layout */
body {
  background-color: #f8f9fa;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.card {
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  margin-bottom: 20px;
  overflow: hidden;
}

.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}

.card-img-top {
  height: 200px;
  object-fit: cover;
}

.card-title {
  font-weight: 600;
  margin-bottom: 0.5rem;
}

.card-text {
  color: #6c757d;
}

.btn-primary {
  background-color: #4361ee;
  border: none;
  padding: 8px 20px;
  border-radius: 5px;
}

.btn-primary:hover {
  background-color: #3a56d4;
}

.dashboard-header {
  padding: 20px 0;
  margin-bottom: 30px;
  border-bottom: 1px solid #e9ecef;
}

@media (max-width: 768px) {
  .card-img-top {
    height: 160px;
  }
}
"""
    
    # Write files
    try:
        with open(html_path, 'w') as f:
            f.write(html_content)
        print(f"Created HTML file: {html_path}")
        
        with open(css_path, 'w') as f:
            f.write(css_content)
        print(f"Created CSS file: {css_path}")
        
        return True
    except Exception as e:
        print(f"Error creating files: {e}")
        return False

def main():
    """Main entry point for the script"""
    parser = argparse.ArgumentParser(description="Direct File Creator - Create HTML and CSS files without VS Code")
    parser.add_argument("--output", "-o", help="Output directory", default=".")
    parser.add_argument("--type", "-t", help="Type of page to create", choices=["price", "card"], required=True)
    
    args = parser.parse_args()
    
    # Convert to absolute path
    output_path = os.path.abspath(args.output)
    
    # Create the output directory if it doesn't exist
    os.makedirs(output_path, exist_ok=True)
    
    # Create the requested page type
    if args.type == "price":
        create_price_page(output_path)
    elif args.type == "card":
        create_card_layout(output_path)

if __name__ == "__main__":
    main()
