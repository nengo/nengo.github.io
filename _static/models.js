function slugify(text) {
  return text.toString().toLowerCase()
    .replace(/\s+/g, '-')           // Replace spaces with -
    .replace(/[^\w\-]+/g, '')       // Remove all non-word chars
    .replace(/\-\-+/g, '-')         // Replace multiple - with single -
    .replace(/^-+/, '')             // Trim - from start of text
    .replace(/-+$/, '');            // Trim - from end of text
}

function getKeywords(item) {
  var keystring = item.values()["model-keywords"];
  keystring = keystring.replace(/<\/em><em>/g, ",");
  keystring = keystring.slice(4, keystring.length - 5);
  return keystring.split(",");
}



$(document).ready(function() {
  // Hide model details by default
  $(".model-details").hide();

  // Show on click
  $(".model.container").click(function() {
    $(this)
      .children(".model-details")
      .slideToggle();
  });

  // But don't show if a link is clicked
  $(".model.container").on("click", "a.external", function(e) {
    e.stopPropagation();
  });

  // Using list.js for list management
  var listObj = new List("nengo-models", {
    listClass: "section",
    page: 100, // We initially set this high so we don't lose non-list items
    pagination: { innerWindow: 4 },
    valueNames: [
      "model-header",
      "model-title",
      "model-date",
      "model-authors",
      "model-keywords",
      "model-details"
    ]
  });
  var filtTest = function(item) {
    return item.elm.classList.contains("model");
  };
  listObj.items = listObj.items.filter(filtTest);
  listObj.matchingItems = listObj.matchingItems.filter(filtTest);
  listObj.visibleItems = listObj.visibleItems.filter(filtTest);

  // A few monkeypatches and hacks to make things work for us
  listObj.templater.clear = function() {
    listObj.items.forEach(function(item) {
      if (listObj.list.contains(item.elm)) {
        listObj.list.removeChild(item.elm);
      }
    });
  };

  // Set the actual pagination value then refresh
  listObj.page = 5;
  listObj.search("");

  // Hook up dropdowns
  $("a#sort-date-asc").click(function(e) {
    e.preventDefault();
    listObj.sort("model-date", {
      sortFunction: function(a, b) {
        var aDate = Date.parse(a.values()["model-date"]);
        var bDate = Date.parse(b.values()["model-date"]);
        return aDate - bDate;
      }
    });
  });
  $("a#sort-date-desc").click(function(e) {
    e.preventDefault();
    listObj.sort("model-date", {
      sortFunction: function(a, b) {
        var aDate = Date.parse(a.values()["model-date"]);
        var bDate = Date.parse(b.values()["model-date"]);
        return bDate - aDate;
      }
    });
  });
  $("a#sort-title").click(function(e) {
    e.preventDefault();
    listObj.sort("model-title");
  });
  $("a#sort-authors").click(function(e) {
    e.preventDefault();
    listObj.sort("model-authors");
  });
  $("a#clear-keywords").click(function(e) {
    e.preventDefault();
    listObj.filter();
  });

  // Get all keywords
  var keywords = {};
  var slugs = [];
  listObj.items.forEach(function(item) {
    getKeywords(item).forEach(function(keyword) {
      var slug = slugify(keyword);
      if (slugs.indexOf(slug) === -1) {
        keywords[slug] = keyword;
        slugs.push(slug);
      }
    });
  });
  slugs.sort();

  // Make dropdown entries for each
  var kwDropdown = $("#filter-dropdown .dropdown-menu");
  slugs.forEach(function(slug) {
    kwDropdown.append(
      '<li><a href="#" id="' + slug + '">' + keywords[slug] + '</a></li>'
    );
    $("a#" + slug).click(function(e) {
      e.preventDefault();
      // Remove any previous filters
      listObj.filter();
      // Apply new filter
      listObj.filter(function(item) {
        var keystrings = getKeywords(item);
        for (var i = 0; i < keystrings.length; i++) {
          if (slugify(keystrings[i]) === slug) {
            return true;
          }
        }
        return false;
      });
    });
  });
});
