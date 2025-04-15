"""
Page Generator Module

This module generates new pages based on existing design patterns,
maintaining consistency with the project's style and layout.
"""

import os
import re
import json
import time
from pathlib import Path
import shutil

class PageGenerator:
    """Generates new pages based on existing design patterns"""

    def __init__(self, project_path, design_analyzer):
        """Initialize the page generator with the project path and design analyzer"""
        self.project_path = project_path
        self.design_analyzer = design_analyzer

        # Create a templates directory if it doesn't exist
        self.templates_dir = os.path.join(project_path, 'knowledge', 'templates')
        os.makedirs(self.templates_dir, exist_ok=True)

    def generate_price_page(self, output_path=None, template_name=None):
        """Generate a price page based on existing design patterns"""
        print("Generating price page based on existing design patterns...")

        # If no output path is specified, use the project root
        if not output_path:
            output_path = self.project_path

        # Make sure the design patterns are loaded
        if not self.design_analyzer.design_patterns['colors']:
            if not self.design_analyzer.load_design_patterns():
                print("No design patterns found. Analyzing project...")
                self.design_analyzer.analyze_project_design('dist')

        # Get design information
        primary_color = self.design_analyzer.get_primary_color()
        font_family = self.design_analyzer.get_font_family()
        bootstrap_version = self.design_analyzer.get_bootstrap_version()
        common_classes = self.design_analyzer.get_common_classes()

        # Determine the Bootstrap CSS URL
        if bootstrap_version:
            bootstrap_css_url = f"https://cdn.jsdelivr.net/npm/bootstrap@{bootstrap_version}/dist/css/bootstrap.min.css"
            bootstrap_js_url = f"https://cdn.jsdelivr.net/npm/bootstrap@{bootstrap_version}/dist/js/bootstrap.bundle.min.js"
        else:
            bootstrap_css_url = "https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css"
            bootstrap_js_url = "https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"

        # Create the HTML file path
        html_file_path = os.path.join(output_path, "price.html")
        css_file_path = os.path.join(output_path, "price.css")

        # Generate the HTML content
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Pricing Plans</title>
  <!-- Bootstrap CSS -->
  <link href="{bootstrap_css_url}" rel="stylesheet">
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
  <script src="{bootstrap_js_url}"></script>
  <!-- Font Awesome -->
  <script src="https://kit.fontawesome.com/a076d05399.js" crossorigin="anonymous"></script>
</body>
</html>
"""

        # Generate the CSS content
        css_content = f"""/* Custom styles for pricing page */
body {{
  background-color: #f8f9fa;
  font-family: {font_family};
}}

.pricing-card-title {{
  font-size: 2.5rem;
  font-weight: 500;
}}

.card {{
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  overflow: hidden;
}}

.card:hover {{
  transform: translateY(-5px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}}

.btn-primary {{
  background-color: {primary_color};
  border-color: {primary_color};
}}

.btn-primary:hover {{
  background-color: {self._darken_color(primary_color)};
  border-color: {self._darken_color(primary_color)};
}}

.btn-outline-primary {{
  color: {primary_color};
  border-color: {primary_color};
}}

.btn-outline-primary:hover {{
  background-color: {primary_color};
  color: white;
}}

.card-header.bg-primary {{
  background-color: {primary_color} !important;
}}

.border-primary {{
  border-color: {primary_color} !important;
}}

.accordion-button:not(.collapsed) {{
  background-color: #e7f1ff;
  color: {primary_color};
}}

.accordion-button:focus {{
  border-color: {primary_color};
  box-shadow: 0 0 0 0.25rem {self._rgba_from_hex(primary_color, 0.25)};
}}

@media (max-width: 768px) {{
  .pricing-card-title {{
    font-size: 2rem;
  }}
}}
"""

        # Write the files
        try:
            with open(html_file_path, 'w') as f:
                f.write(html_content)
            print(f"Created HTML file: {html_file_path}")

            with open(css_file_path, 'w') as f:
                f.write(css_content)
            print(f"Created CSS file: {css_file_path}")

            return html_file_path
        except Exception as e:
            print(f"Error creating files: {e}")
            return None

    def _darken_color(self, hex_color, factor=0.1):
        """Darken a hex color by a factor"""
        # Check if it's a valid hex color
        if not hex_color.startswith('#') or not all(c in '0123456789ABCDEFabcdef' for c in hex_color.lstrip('#')):
            return "#3a56d4"  # Default darker blue

        # Remove the # if present
        hex_color = hex_color.lstrip('#')

        # Make sure it's a valid hex color
        if len(hex_color) != 6:
            return "#3a56d4"  # Default darker blue

        try:
            # Convert to RGB
            r = int(hex_color[0:2], 16)
            g = int(hex_color[2:4], 16)
            b = int(hex_color[4:6], 16)

            # Darken
            r = max(0, int(r * (1 - factor)))
            g = max(0, int(g * (1 - factor)))
            b = max(0, int(b * (1 - factor)))

            # Convert back to hex
            return f"#{r:02x}{g:02x}{b:02x}"
        except ValueError:
            return "#3a56d4"  # Default darker blue

    def _rgba_from_hex(self, hex_color, alpha=1.0):
        """Convert a hex color to rgba"""
        # Check if it's a valid hex color
        if not hex_color.startswith('#') or not all(c in '0123456789ABCDEFabcdef' for c in hex_color.lstrip('#')):
            return f"rgba(67, 97, 238, {alpha})"  # Default blue with alpha

        # Remove the # if present
        hex_color = hex_color.lstrip('#')

        # Make sure it's a valid hex color
        if len(hex_color) != 6:
            return f"rgba(67, 97, 238, {alpha})"  # Default blue with alpha

        try:
            # Convert to RGB
            r = int(hex_color[0:2], 16)
            g = int(hex_color[2:4], 16)
            b = int(hex_color[4:6], 16)

            # Return rgba
            return f"rgba({r}, {g}, {b}, {alpha})"
        except ValueError:
            return f"rgba(67, 97, 238, {alpha})"  # Default blue with alpha
