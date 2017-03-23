// select node data for name,screen_name,image show
// d3.select(your_node).datum();
// $(function(ready){

	// get the data
	// $(".svg-section").width();

	function drawGraph(filename,checkFriendships){

	var width = $(".svg-section").width(),
	    height = 700;

	var svg = d3.select(".svg-section").append("svg")
	    .attr("width", width)
	    .attr("height", height);


	var force = d3.layout.force()
	    .gravity(.05)
	    .distance(100)
	    .charge(-100)
	    .size([width, height]);

	d3.json(filename, function(error, json) {
	  	var edges = [];
	    json.links.forEach(function(e) { 
		    var sourceNode = json.nodes.filter(function(n) { return n.id === e.source; })[0],
		    targetNode = json.nodes.filter(function(n) { return n.id === e.target; })[0];
		    	
		    edges.push({source: sourceNode, target: targetNode, value: e.Value});
	    });

	  force
	      .nodes(json.nodes)
	      .links(edges)
	      .linkDistance(200)
	      .start();

	  var link = svg.selectAll(".link")
	      .data(edges)
		  .enter().append("line")
	      .attr("class", "link");

	  var node = svg.selectAll(".node")
	      .data(json.nodes)
	    .enter().append("g")
	      .attr("class", "node")
	      .on("mouseover", function(d){
	      		  d3.select(this).select("circle").transition()
			      .duration(750)
			      .attr("r", 16);
			  
			  var content = '<h5>Last Hovered Node</h5>'
			   content += '<h6>Name:</br> ' + d.name + '</span></h6>';
			   content += '<h6>Screen Name:</br> ' + d.id + '</span></h6></br>';
			   content += '<div class="row"><div class="col-sm-12"><a target="_blank" href="https://twitter.com/'+d.id+'"><img src=' + d.image + 
			   ' alt="" class="center-element" style="max-width:100%;max-height:50px;"></a></div>';
			  if(checkFriendships){
			  	content += '<div class="col-sm-12"><h5>Following:</h5>';

			  var followedBy = [];
			  for(var i in edges){
	      		var tempID = edges[i]["source"]["id"];
	      		var tempTargetID = edges[i]["target"]["id"];
	      		if(tempID == d.id){
	      			content+= edges[i]["target"]["id"]+'</br>';
	      		}
	      		if(tempTargetID == d.id){
	      			followedBy.push(edges[i]["source"]["id"])
	      		}
		      }

			  content+= '</div><div class="col-sm-12"><h5>Followed By:</h5>';
			  for(var i in followedBy){
			  	content+=followedBy[i]+'</br>';
			  }

			  content += '</div></div>'
			}else{
				content += '</div>';
			}
			  $("#user-popup").html(content);
			  $("#user-popup").show();
	      })
		  .on("mouseout", mouseout)
	      .call(force.drag);

	  node.append("image")
      .attr("xlink:href", function(d){return d.image;})
      .attr("x", -8)
      .attr("y", -8)
      .attr("width", 24)
      .attr("height", 24);

	  // node.append("svg:p")
	  //     .append("text")
	  //     .attr("dx", 12)
	  //     .attr("dy", ".35em")
	  //     .text(function(d) { return d.name})

	  
	  force.on("tick", function() {
	    link.attr("x1", function(d) { return d.source.x; })
	        .attr("y1", function(d) { return d.source.y; })
	        .attr("x2", function(d) { return d.target.x; })
	        .attr("y2", function(d) { return d.target.y; });


	    node.attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });
	  });


	function mouseout() {
	  d3.select(this).select("circle").transition()
	      .duration(750)
	      .attr("r", 8);
	}

	});
}
// drawGraph("data/allFollowersGraph.json",false);

// });

