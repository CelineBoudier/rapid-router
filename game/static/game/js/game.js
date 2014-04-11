function createDefaultLevel(){

	  var points = [
	  		[0, 4],
		  	[1, 4],
		  	[1, 3],
		  	[1, 2],
		  	[2, 2],
		  	[3, 2],
		  	[3, 1],
		  	[3, 0],
		  	[4, 0],
		  	[5, 0],
		  	[5, 1],
		  	[5, 2],
		  	[6, 2],
		  	[7, 2],
		  	[8, 2],
	  ]

	  var previousNode = null;
	  var nodes = [];
	  for (var i = 0; i < points.length; i++) {
	      var p = points[i];
	      var coordinate = new Coordinate(p[0], p[1]);
	      var node = new Node(coordinate);
	      if (previousNode) {
	          node.addConnectedNodeWithBacklink(previousNode);
	      }
	      previousNode = node;
	      nodes.push(node);
	  }
	  var map = new Map(nodes);
	  var van = new Van(nodes[0], nodes[1]);
	  return new Level(map, van, nodes[nodes.length - 1]);
}

function defaultProgram(level){
	  var program = new Program(
	          [TURN_LEFT,
	              FORWARD,
	              TURN_RIGHT,
	              FORWARD,
	              TURN_LEFT,
	              FORWARD,
	              TURN_RIGHT,
	              FORWARD,
	              TURN_RIGHT,
	              FORWARD,
	              TURN_LEFT,
	              FORWARD,
	              FORWARD,
	              FORWARD
	          ]);
	
	  level.play(program);
}

function trackDevelopment(level){
	var program = new Program([]);
	
	$('#moveForward').click(function(){
		program.instructions.push(FORWARD);
    });
	
    $('#turnLeft').click(function(){
    	program.instructions.push(TURN_LEFT);
    });

    $('#turnRight').click(function(){
		program.instructions.push(TURN_RIGHT);
	});
    
    $('#play').click(function(){
    	level.play(program);
	});
}

$(function() {
    'use strict';
    
    var level = createDefaultLevel();
    
    $('#runDefaultProgram').click(function(){
    	defaultProgram(level);
	});

    trackDevelopment(level);
});