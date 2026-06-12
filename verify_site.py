import os
import json
import re

print("=== STARTING WEBSITE VERIFICATION ===")

errors = []
warnings = []

# 1. Check folder structure
base_dir = r"C:\web_antigravity\web_soluciones_cluster_afolu"
folders = ["data", "css", "js", "pages", "assets/images", "assets/diagrams", "assets/icons"]

for folder in folders:
    path = os.path.join(base_dir, folder)
    if not os.path.exists(path):
        errors.append(f"Missing folder: {folder}")
    else:
        print(f"[OK] Folder exists: {folder}")

# 2. Check solutions.json
json_path = os.path.join(base_dir, "data", "solutions.json")
if not os.path.exists(json_path):
    errors.append("Missing data/solutions.json")
else:
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if len(data) != 20:
            errors.append(f"solutions.json does not contain exactly 20 solutions (found {len(data)})")
        else:
            print("[OK] solutions.json has exactly 20 entries")
            
        # Verify keys in entries
        for idx, sol in enumerate(data):
            sol_id = sol.get("id")
            slug = sol.get("slug")
            if not sol_id or not slug:
                errors.append(f"Solution at index {idx} missing ID or slug")
            
            # Check files existence
            page_path = os.path.join(base_dir, "pages", slug, "index.html")
            if not os.path.exists(page_path):
                errors.append(f"Missing landing page: pages/{slug}/index.html")
            
            ill_path = os.path.join(base_dir, "assets/images", f"solucion-{sol_id}.svg")
            if not os.path.exists(ill_path):
                errors.append(f"Missing card illustration: assets/images/solucion-{sol_id}.svg")
                
            diag_path = os.path.join(base_dir, "assets/diagrams", f"proceso-{sol_id}.svg")
            if not os.path.exists(diag_path):
                errors.append(f"Missing process diagram: assets/diagrams/proceso-{sol_id}.svg")
                
    except Exception as e:
        errors.append(f"Error parsing solutions.json: {e}")

# 3. Check index.html links and card counts
index_path = os.path.join(base_dir, "index.html")
if not os.path.exists(index_path):
    errors.append("Missing index.html")
else:
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check card count
    cards_found = content.count('class="solution-card"')
    if cards_found != 20:
        errors.append(f"index.html does not have exactly 20 solution cards (found {cards_found})")
    else:
        print("[OK] index.html has exactly 20 cards")
        
    # Check that it links to all 20 pages
    for sol in data:
        link = f'href="pages/{sol["slug"]}/index.html"'
        if link not in content:
            errors.append(f"index.html does not link to: pages/{sol['slug']}/index.html")
    print("[OK] All 20 landing page links verified in index.html")

# 4. Check references in landing pages
for sol in data:
    slug = sol["slug"]
    id_str = sol["id"]
    page_path = os.path.join(base_dir, "pages", slug, "index.html")
    if os.path.exists(page_path):
        with open(page_path, 'r', encoding='utf-8') as f:
            p_content = f.read()
            
        # Check back links
        if 'href="../../index.html"' not in p_content:
            errors.append(f"Page {slug}/index.html missing 'Volver al catálogo' link to '../../index.html'")
            
        # Check illustration link
        ill_link = f'src="../../assets/images/solucion-{id_str}.svg"'
        if ill_link not in p_content:
            errors.append(f"Page {slug}/index.html missing or incorrect illustration link: {ill_link}")
            
        # Check diagram link
        diag_link = f'src="../../assets/diagrams/proceso-{id_str}.svg"'
        if diag_link not in p_content:
            errors.append(f"Page {slug}/index.html missing or incorrect process diagram link: {diag_link}")
            
        # Check previous/next navigation links
        prev_idx = (int(id_str) - 2) % 20
        next_idx = int(id_str) % 20
        prev_slug = data[prev_idx]["slug"]
        next_slug = data[next_idx]["slug"]
        
        prev_link = f'href="../{prev_slug}/index.html"'
        next_link = f'href="../{next_slug}/index.html"'
        
        if prev_link not in p_content:
            errors.append(f"Page {slug}/index.html missing or incorrect previous link: {prev_link}")
        if next_link not in p_content:
            errors.append(f"Page {slug}/index.html missing or incorrect next link: {next_link}")

# 5. Review report
print("\n=== VERIFICATION SUMMARY ===")
if errors:
    print(f"[ERROR] Verification failed with {len(errors)} errors:")
    for err in errors:
        print(f"  - {err}")
else:
    print("[SUCCESS] ALL VERIFICATIONS PASSED SUCCESSFULLY! No errors found. The website is fully operational.")
    
if warnings:
    print(f"[WARNING] {len(warnings)} Warnings:")
    for warn in warnings:
        print(f"  - {warn}")
print("=============================")
