---
title: Add your own resources
tags: [Central themes, Resources]
---
<div class="resources-board">
  {% for resource in resources() %}
        <div class="resource-box">
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
            {{ resource.theme | replace("-", " ") | title }}            </div>
        </div>
    {% endfor %}
</div>


<!-- Box for users to submit a new resource -->
<div class="resources-submit-box">

  <p class="resources-submit-description">
    Have a resource to share?
  </p>

  <p class="resources-submit-helper">
    We'd love to hear about websites, tools, guides, or other resources you've found useful. Tell us a little about what makes it worth sharing.
  </p>

  <p class="resources-submit-helper">
    </br>
    After clicking <strong>Submit</strong>, a GitHub issue will open
    with your resource pre-filled. Simply click <strong>"Create"</strong>
    to send it to the CAKE team for review before it goes live.
  </p>

  <input
    class="tip-input"
    id="resource-title"
    placeholder="Resource title"
  />

  <input
    class="tip-input"
    id="resource-url"
    placeholder="Paste the resource link"
  />

  <textarea
    class="tip-textarea"
    id="resource-comment"
    placeholder="What makes this resource useful? Tell us a little about it..."
  ></textarea>

<label for="resource-theme">What theme does this resource fit under?</label>

  <select
    id="resource-theme"
    onchange="toggleCustomTheme(); updateSubthemes();"
  >

  <option value="">Select a theme...</option>

  {% for theme in themes() %}
    <option value="{{ theme }}">
      {{ theme | replace("-", " ") | title }}
    </option>
  {% endfor %}

  <option value="other">Other — suggest a new theme</option>
</select>

<input
  id="custom-theme"
  class="tip-input"
  placeholder="Enter a new theme"
  style="display: none;"
/>

<div class="subtheme-picker">
  <div class="subtheme-label">
    Sub-themes <span>(optional)</span>
  </div>

  <div class="subtheme-grid">
    {% for theme in themes() %}
      <label
        class="subtheme-option"
        data-theme="{{ theme }}"
      >
        <input
          type="checkbox"
          name="subthemes"
          value="{{ theme }}"
        >
        <span>{{ theme | replace("-", " ") | title }}</span>
      </label>
    {% endfor %}
  </div>
</div>

<button
class="tip-submit-btn"
onclick="submitResource()">
Submit
</button>
</div>



<!-- Script that takes the user input and creates the issue -->
<script>

function updateSubthemes() {

  const selectedTheme =
    document.getElementById("resource-theme").value;

  document
    .querySelectorAll(".subtheme-option")
    .forEach(option => {

      const checkbox =
        option.querySelector("input");

      if (option.dataset.theme === selectedTheme) {

        // Don't allow the primary theme
        // to also be selected as a sub-theme
        option.style.display = "none";
        checkbox.checked = false;

      } else {

        option.style.display = "";

      }

    });
}

function toggleCustomTheme() {
  const themeSelect = document.getElementById("resource-theme");
  const customTheme = document.getElementById("custom-theme");

  if (themeSelect.value === "other") {
    customTheme.style.display = "block";
  } else {
    customTheme.style.display = "none";
    customTheme.value = "";
  }
}

function submitResource() {
  const title = document
    .getElementById("resource-title")
    .value
    .trim();

  let url = document
    .getElementById("resource-url")
    .value
    .trim();

  const comment = document
    .getElementById("resource-comment")
    .value
    .trim();

  const selectedTheme = document
    .getElementById("resource-theme")
    .value;

  // Add https:// 
  if (url && !url.startsWith("http://") && !url.startsWith("https://")) {
    url = "https://" + url;
  }

  let theme;

  if (selectedTheme === "other") {
    theme = document
      .getElementById("custom-theme")
      .value
      .trim()
      .toLowerCase()
      .replace(/\s+/g, "-");
  } else {
    theme = selectedTheme;
  }

  const subthemes =
    Array.from(
      document.querySelectorAll(
        'input[name="subthemes"]:checked'
      )
    ).map(
      checkbox => checkbox.value
    );


  if (!title || !url || !comment || !theme) {
    alert("Please fill in all fields.");
    return;
  }

  if (!url.includes("www.")) {
    alert("Please enter a URL that includes www.");
    return;
  }
  
  const issueTitle = `[Resource:${theme}] ${title}`;

  const issueBody =
`type: resource
title: ${title}
url: ${url}
comment: ${comment}
theme: ${theme}`;

  // Only add subthemes if the user selected any
  if (subthemes.length > 0) {

    issueBody +=
`\nsubthemes:`;

    subthemes.forEach(subtheme => {

      issueBody +=
`\n  - ${subtheme}`;

    });

  }

  const githubUrl =
    "https://github.com/eleanor-broadway/CAKEbox/issues/new"
    + "?labels=resource-submission"
    + "&title=" + encodeURIComponent(issueTitle)
    + "&body=" + encodeURIComponent(issueBody);

  window.open(githubUrl, "_blank");
}
</script>