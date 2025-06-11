// custom code for displaying garden search results from Lunr
function displayResults (qterms, results, store) {
  const searchResultsSummary = document.getElementById('search-results-summary')
  const searchResultsList = document.getElementById('search-results-list')
  if (results.length) {
    searchResultsSummary.innerHTML = results.length + ' result' + (results.length == 1 ? '' : 's') + ' found for <em>' + q + '</em>:'
    let resultList = ''
    // Iterate and build result list elements
    for (const n in results) {
      const item = store[results[n].ref]
      resultList += '<article class="list__item post">'

      // breadcrumbs
      resultList += '<div class="smallcrumbs">' + item.smallcrumbs + '</div>'

      // linked title
      resultList += '<h3 class="list__title post__title"><a href="' + item.url + '">' + item.title + '</a>' +
       (item.draft? ' (DRAFT)' : '') + '</h3>'

      // normalize diacritics for better snippet matching
      let content = item.content.normalize("NFD").replace(/[\u0300-\u036f]/g, "")

      // find text around first instance of first query term
      let q1 = qterms[0].normalize("NFD").replace(/[\u0300-\u036f]/g, "")
      let re = new RegExp(`^.*?(.{0,140})(${q1})(.{0,140}).*?$`, 'is')
      // extract and highlight first term
      let snippet = content.replace(re, '$1<em>$2</em>$3')
      // highlight any other terms found within the snippet
      console.log(qterms)
      if (qterms.length > 1) {
        for (let i = 1 ; i < qterms.length; i++) {
          let qi = qterms[i]
          let re2 = new RegExp(`(${qi})`, 'i')
          snippet = snippet.replace(re2, '<em>$1</em>')
        }
      }
      snippet = '...' + snippet.replace(/^\w+|\w+$/g, '') + '...'
      resultList += snippet

      resultList += '</article>'
    }
    searchResultsList.innerHTML = resultList
  } else {
    searchResultsSummary.innerHTML = 'No results found for <b>' + q + '</b>'
    searchResultsList.innerHTML = ''
  }
}

// Get the query parameter(s)
const params = new URLSearchParams(window.location.search)
let q = params.get('q')

// Perform a search if there is a query
if (q) {

  // Retain the search input in the form when displaying results
  window.setTimeout((function(){document.getElementById('search-input').setAttribute('value', q)}), 500)

  const idx = lunr(function () {
    this.ref('id')
    this.field('title', {
      boost: 10
    })
    this.field('content')

    for (const key in window.store) {
      this.add({
        id: key,
        title: window.store[key].title,
        content: window.store[key].content
      })
    }
  })

  // Only return results that contain ALL query terms
  let qterms = q.normalize("NFD").replace(/[\u0300-\u036f]/g, "").replace(/\W+/g, ' ').trim().split(' ')
  let qall = '+' + qterms.join(' +')

  try {
    // Perform the search
    const results = idx.search(qall)
    // Update the list with results
    displayResults(qterms, results, window.store)
  }
  catch {
    const searchResultsSummary = document.getElementById('search-results-summary')
    searchResultsSummary.innerHTML = 'Error parsing the query <b>' + q + '</b>'
    searchResultsList = document.getElementById('search-results-list').innerHTML = ''
  }
}
