---
title: Collaboration
tags: [Key Themes]
---

This theme is all about making collaborations feel easier, smoother and more effective. How can we support meaningful engagement and lasting collaboration, focusing on how we exchange knowledge effectively, learn from one another, and build sustainable, long-term partnerships across the DRI landscape.

<!-- Enable filtering for keywords, theme is fixed -->
<div class="resources-filter">
  <label for="keyword-filter"><b>Filter by keyword:</b></label>
  <select
    id="keyword-filter"
    class="tip-input"
    onchange="filterResources()"
    disabled
  >
    <option value="">All keywords</option>
  </select>
</div>
<br>


<!-- Show sprinkles -->
<div class="sticky-board">
  {% for tip in tips() %}
    {% if tip.theme == "collaboration" or "collaboration" in tip.keywords %}
    <div class="sticky-note {{ tip.color }}"
            data-theme="{{ tip.theme }}"
            data-keywords="{{ tip.keywords | join(',') }}"
        >
        <div class="note-title">
        {{ tip.emoji }} {{ tip.title }}
        </div>

        <div class="note-text">
        {{ tip.text }}
        </div>
    </div>
{% endif %}
{% endfor %}
</div>


<!-- Show resources -->
<div class="resources-board">
  {% for resource in resources() %}
    {% if resource.theme == "collaboration" or "collaboration" in resource.keywords %}
        <div
        class="resource-box"
        data-theme="{{ resource.theme }}"
        data-keywords="{{ resource.keywords | join(',') }}"
        >
        <div class="resource-title">
            {{ resource.title }}
        </div>

        <div class="resource-url">
            <a href="{{ resource.url }}">{{ resource.url }}</a>
        </div>

        <div class="resource-text">
            {{ resource.comment }}
        </div>

        <div class="theme-badge">
            {{ resource.theme }}
        </div>
        
        {% if resource.keywords %}
            <div class="resource-keywords">
                {% for keyword in resource.keywords %}
                <span class="resource-keyword">{{ keyword }}</span>
                {% endfor %}
            </div>
        {% endif %}
    
        </div>

    {% endif %}
  {% endfor %}
</div>

<br>

**Interested in our other themes? [Explore all resources here.](../all.md)**

!!! question "Have something to share?"
    Check out our [Contributing Guide](/CAKEbox/docs/how-to-contribute/index.md) for our quick and easy ways to add your own resources.  



<!-- Optional keyword filter for resources and sticky notes -->
<script>
function updateKeywordFilter() {
  const keywordFilter = document.getElementById("keyword-filter");
  const previousKeyword = keywordFilter.value;
  const keywords = new Set();

  document.querySelectorAll(".resource-box, .sticky-note")
    .forEach(item => {
      (item.dataset.keywords || "").split(",").forEach(keyword => {
        const cleaned = keyword.trim();
        if (cleaned && cleaned !== "tools") {
          keywords.add(cleaned);
        }
      });
    });

  keywordFilter.innerHTML = '<option value="">All keywords</option>';
  keywordFilter.disabled = false;

  [...keywords].sort().forEach(keyword => {
    const option = document.createElement("option");
    option.value = keyword;
    option.textContent = keyword;
    keywordFilter.appendChild(option);
  });

  if (keywords.has(previousKeyword)) {
    keywordFilter.value = previousKeyword;
  }
}

function filterResources() {
  const selectedKeyword = document.getElementById("keyword-filter").value;

  document.querySelectorAll(".resource-box, .sticky-note")
    .forEach(item => {
      const keywords = (item.dataset.keywords || "")
        .split(",")
        .map(k => k.trim());

      item.style.display =
        !selectedKeyword || keywords.includes(selectedKeyword) ? "" : "none";
    });
}

document.addEventListener("DOMContentLoaded", () => {
  updateKeywordFilter();
  filterResources();
});
</script>
