import json

projects = [
    {"name": "Effectiva", "tag": "Websites", "desc": "Custom Shopify store for UAE client with theme customization and product setup", "url": "http://effectiva.ae", "initial": "E", "color": "#96BF48", "subtag": "Shopify"},
    {"name": "Triton Interior", "tag": "Websites", "desc": "Interior design eCommerce store with custom product fields and payment integration", "url": "https://tritoninterior.com", "initial": "T", "color": "#E8441A", "subtag": "WooCommerce"},
    {"name": "Saraakshi", "tag": "Websites", "desc": "Full eCommerce store with custom fields and advanced WooCommerce setup", "url": "https://saraakshi.com", "initial": "S", "color": "#E8441A", "subtag": "WooCommerce"},
    {"name": "Al Safa Home Services", "tag": "Websites", "desc": "Service website for Kuwait-based home services company", "url": "https://alsafahomeserviceskuwait.com", "initial": "A", "color": "#0073AA", "subtag": "Service"},
    {"name": "Treasure Valley", "tag": "Websites", "desc": "Business website with custom design and WordPress CMS", "url": "https://treasurevalley.online", "initial": "T", "color": "#888888", "subtag": "WordPress"},
    {"name": "Fortune Banasura Resort", "tag": "Websites", "desc": "Resort website with booking UI, gallery, and room showcase", "url": "https://fortunebanasura-resort.vercel.app", "initial": "F", "color": "#E8A21A", "subtag": "Resort"},
    {"name": "Hotels by Green View", "tag": "Websites", "desc": "Hotel listing website with room details and booking information", "url": "https://hotelsbygreenview.com", "initial": "H", "color": "#2E7D32", "subtag": "Hotel"},
    {"name": "B&B Moderns", "tag": "Websites", "desc": "Modern business website built with WordPress and Elementor", "url": "https://bandbmoderns.com", "initial": "B", "color": "#1A1A1A", "subtag": "WordPress"},
    {"name": "Orange International", "tag": "Websites", "desc": "Corporate website for international business with SEO optimization", "url": "https://orangeinternational.in", "initial": "O", "color": "#E8441A", "subtag": "Corporate"},
    {"name": "Bizora Business", "tag": "Websites", "desc": "UAE-based business website with service pages and contact forms", "url": "https://bizorabusiness.com", "initial": "B", "color": "#0073AA", "subtag": "Business"},
    {"name": "Bhive Storage", "tag": "Websites", "desc": "Storage solutions company website with service listings", "url": "https://bhivestorage.com", "initial": "B", "color": "#E8A21A", "subtag": "Storage"},
    {"name": "Sahanai Pediatric Dentist", "tag": "Websites", "desc": "UAE dental clinic website with appointment and service info", "url": "https://sahanaipediatricdentist.com", "initial": "S", "color": "#2196F3", "subtag": "Clinic"},
    {"name": "Royal Drains", "tag": "Websites", "desc": "Canada-based drainage services company website", "url": "https://royaldrains.namecast.ca", "initial": "R", "color": "#1A1A1A", "subtag": "Service"},
    {"name": "Namecast", "tag": "Websites", "desc": "Canadian business website with full WordPress setup", "url": "https://namecast.ca", "initial": "N", "color": "#888888", "subtag": "Business"},
    {"name": "Inspite Technologies", "tag": "Websites", "desc": "Company website for Inspite Technologies, Infopark Kochi", "url": "https://inspitetech.com", "initial": "I", "color": "#E8441A", "subtag": "Corporate"},
    {"name": "Aura Fashions", "tag": "React", "desc": "Modern fashion eCommerce frontend built with React.js and Vercel", "url": "https://aurafashions.vercel.app", "initial": "A", "color": "#61DAFB", "subtag": "React.js"},
    {"name": "H2O Lifestyle", "tag": "React", "desc": "Lifestyle brand frontend with clean UI and product showcase", "url": "https://h2o-lifestyle.vercel.app", "initial": "H", "color": "#0073AA", "subtag": "React.js"},
    {"name": "H2O Admin Panel", "tag": "Dashboards", "desc": "Admin dashboard for H2O Lifestyle with inventory management", "url": "https://h2o-lifestyle.vercel.app/admin", "initial": "H", "color": "#0073AA", "subtag": "Admin"},
    {"name": "Future Link Media", "tag": "React", "desc": "Media agency website built with React.js and modern animations", "url": "https://future-link-media.vercel.app", "initial": "F", "color": "#9C27B0", "subtag": "React.js"},
    {"name": "Scorio Product UI", "tag": "React", "desc": "Product detail page UI with elegant design and interactions", "url": "https://scorio-three.vercel.app/product/elysiangold-pendant-light-modern", "initial": "S", "color": "#E8A21A", "subtag": "UI/UX"},
    {"name": "Resource Management System", "tag": "Dashboards", "desc": "Full resource tracking and management system with admin controls", "url": "https://inspite-resource-system.vercel.app", "initial": "R", "color": "#E8441A", "subtag": "System"},
    {"name": "Hotel Booking Management", "tag": "Dashboards", "desc": "Complete hotel booking admin dashboard with real-time data views", "url": "https://hotel-booking-managementtau.vercel.app", "initial": "H", "color": "#2E7D32", "subtag": "Admin"},
    {"name": "Taxi Admin Dashboard", "tag": "Dashboards", "desc": "Taxi fleet management admin panel with driver and ride tracking", "url": "https://my-taxi-admin-prototype-demo.surge.sh", "initial": "T", "color": "#E8A21A", "subtag": "Fleet"},
    {"name": "Courier Admin Panel", "tag": "Dashboards", "desc": "Global courier management system with shipment tracking dashboard", "url": "https://global-courier-admin.vercel.app", "initial": "C", "color": "#1A1A1A", "subtag": "Logistics"},
    {"name": "Site Management Dashboard", "tag": "Dashboards", "desc": "Construction site management dashboard with project tracking", "url": "https://site-pro-demo.vercel.app", "initial": "S", "color": "#888888", "subtag": "Management"},
    {"name": "League Dashboard UI", "tag": "Dashboards", "desc": "Sports league admin dashboard with team and match management", "url": "https://tspl-league-designgold.vercel.app/dashboard", "initial": "L", "color": "#E8A21A", "subtag": "Sports"},
    {"name": "Thekkinte Nadu Admin", "tag": "Dashboards", "desc": "Community organization admin panel with member management", "url": "https://thekkinte-nadu-admin.vercel.app", "initial": "T", "color": "#2196F3", "subtag": "Community"},
    {"name": "Temple Management System", "tag": "PHP", "desc": "Custom PHP system for temple operations, events and donations", "url": "https://temple.nandanasunil.in", "initial": "T", "color": "#787CB5", "subtag": "PHP"}
]

gradients = [
    "linear-gradient(135deg, #EBF5F0, #D2E8D7)", # Soft Green
    "linear-gradient(135deg, #E6F0FA, #C8E1FA)", # Soft Blue
    "linear-gradient(135deg, #F0E6FA, #DCC8FA)", # Soft Purple
    "linear-gradient(135deg, #F0F0FA, #DCDCF5)", # Soft Grey/Purple
    "linear-gradient(135deg, #FAF0E6, #F5DCC8)", # Soft Orange
    "linear-gradient(135deg, #E6FAF0, #C8F5DC)"  # Soft Teal
]

primary_icons = {
    "Websites": "ri-window-line",
    "React": "ri-reactjs-line",
    "Dashboards": "ri-dashboard-line",
    "PHP": "ri-code-s-slash-line"
}

html = ""
for i, p in enumerate(projects):
    grad = gradients[i % len(gradients)]
    p_icon = primary_icons.get(p['tag'], "ri-window-line")
    
    s_icon = "ri-stack-line"
    sub = p['subtag'].lower()
    if "shopify" in sub: s_icon = "ri-shopping-bag-line"
    elif "woocommerce" in sub or "ecommerce" in sub: s_icon = "ri-shopping-cart-line"
    elif "service" in sub: s_icon = "ri-tools-line"
    elif "wordpress" in sub: s_icon = "ri-wordpress-line"
    
    html += f'''        <div class="project-card glass-card" data-category="{p['tag']}" style="background: {grad};">
          <div class="card-header">
            <div class="card-icons">
              <div class="icon-box"><i class="{p_icon}" style="color: {p['color']};"></i></div>
              <div class="icon-box"><i class="{s_icon}" style="color: var(--dark);"></i></div>
            </div>
            <button class="heart-btn"><i class="ri-heart-line"></i></button>
          </div>
          <div class="card-body">
            <h3 class="project-title">{p['name']}</h3>
            <p class="project-desc">{p['desc']}</p>
          </div>
          <div class="card-footer">
            <a href="{p['url']}" target="_blank" class="view-badge">
              <i class="ri-play-circle-fill"></i> View Project
            </a>
          </div>
        </div>\n'''

with open('projects.html', 'w', encoding='utf-8') as f:
    f.write(html)
