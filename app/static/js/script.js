$(function() {
  var page = location.pathname.split('/')[1]
  var activeNavItem = $('nav ul span#nav-' + page)
  console.log('nav ul span#nav-' + page)
  activeNavItem.addClass('nav-item-active')
})