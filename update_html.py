import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

with open('projects.html', 'r', encoding='utf-8') as f:
    projects_html = f.read()

# 1. CSS for filters
css_to_insert = """
/* PROJECT FILTERS */
.project-filters {
  display: flex;
  justify-content: center;
  gap: 15px;
  margin-bottom: 40px;
  flex-wrap: wrap;
}
.filter-btn {
  padding: 8px 24px;
  border: 1px solid var(--border);
  background: white;
  color: var(--dark);
  border-radius: 30px;
  cursor: pointer;
  font-family: 'Barlow', sans-serif;
  font-weight: 500;
  font-size: 15px;
  transition: all 0.3s ease;
}
.filter-btn.active, .filter-btn:hover {
  background: var(--orange);
  color: white;
  border-color: var(--orange);
}
"""

content = content.replace("/* PROJECTS SECTION */", css_to_insert + "\n/* PROJECTS SECTION */")

# 2. HTML for filters
html_to_insert = """      <div class="project-filters" data-aos>
        <button class="filter-btn active" data-filter="all">All</button>
        <button class="filter-btn" data-filter="Websites">Websites</button>
        <button class="filter-btn" data-filter="React">React</button>
        <button class="filter-btn" data-filter="Dashboards">Dashboards</button>
        <button class="filter-btn" data-filter="PHP">PHP</button>
      </div>
      <div class="projects-grid">"""

content = content.replace('<div class="projects-grid">', html_to_insert)

# 3. Replace Projects Grid Content
# Find the block from <!-- Project 1 --> to the end of projects-grid
start_marker = "<!-- Project 1 -->"
end_marker = "</div>\n    </div>\n  </section>"
start_idx = content.find(start_marker)
end_idx = content.find(end_marker, start_idx)

if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + projects_html + "      " + content[end_idx:]

# 4. JS for filters
js_to_insert = """
  // Project Filtering
  const filterBtns = document.querySelectorAll('.filter-btn');
  const projectCards = document.querySelectorAll('.project-card');

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      // Remove active class from all
      filterBtns.forEach(b => b.classList.remove('active'));
      // Add active class to clicked
      btn.classList.add('active');

      const filterValue = btn.getAttribute('data-filter');

      projectCards.forEach(card => {
        const category = card.getAttribute('data-category');
        if (filterValue === 'all' || filterValue === category) {
          card.style.display = 'block';
          gsap.fromTo(card, {opacity: 0, y: 20}, {opacity: 1, y: 0, duration: 0.5});
        } else {
          card.style.display = 'none';
        }
      });
      // Refresh ScrollTrigger after layout changes
      ScrollTrigger.refresh();
    });
  });
"""

content = content.replace("// GSAP Animations", js_to_insert + "\n  // GSAP Animations")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
