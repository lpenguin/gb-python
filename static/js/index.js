$(function(){
  var search = $("#search");
  $.get('/api/tags', function(json){
    console.log(json);
    var tags = json.result;

    var options = tags.map(function(item){
        return {
          text: '123',
          value: '123'
        }
      })

    var $select = search.selectize({
      create: true,
      options: options
    })

    console.log($select)
  })
})
