$(document).ready(function()
{
    function charger1()
    {
        var jsonStr = $("#json_str").text();

        var data = jQuery.parseJSON(jsonStr.replace(/&quot;/g,'"'));

        //console.log(data.centroid);

        var margins = {
          "left": 40,
          "right": 30,
          "top": 30,
          "bottom": 30
        };

        var width = 500;
        var height = 500;

        var colors = d3.scale.category10();

        var svg = d3.select("#scatter-load").append("svg").attr("width", width + margins.left + margins.right).attr("height", height + margins.top + margins.bottom).append("g")
          .attr("transform", "translate(" + margins.left + "," + margins.top + ")");

        var x = d3.scale.linear()
          .domain(d3.extent(data.obs, function (d) {
          return d.x;
        })).range([0, width - margins.left - margins.right]);

        var y = d3.scale.linear()
          .domain(d3.extent(data.obs, function (d) {
          return d.y;
        })).range([height - margins.top - margins.bottom, 0]);

        svg.append("g").attr("class", "x axis").attr("transform", "translate(0," + y.range()[0] + ")");
        svg.append("g").attr("class", "y axis");


        var xAxis = d3.svg.axis().scale(x).orient("bottom");
        var yAxis = d3.svg.axis().scale(y).orient("left");

        svg.selectAll("g.y.axis").call(yAxis);
        svg.selectAll("g.x.axis").call(xAxis);

        svg.selectAll(".dot")
        .data(data.obs)
        .enter().append("circle")
        .attr("class", "dot")
        .attr("r", 3.5)
        .attr("cx", function(d) { return x(d.x); })
        .attr("cy", function(d) { return y(d.y); })
        .style("fill", function(d) { return colors(d.number); });

        var legend = svg.selectAll(".legend")
          .data(colors.domain())
          .enter().append("g")
          .attr("class", "legend")
          .attr("transform", function(d, i) { return "translate(0," + i * 20 + ")"; });

        legend.append("rect")
        .attr("x", width - 18)
        .attr("width", 18)
        .attr("height", 18)
        .style("fill", colors);

        legend.append("text")
        .attr("x", width - 24)
        .attr("y", 9)
        .attr("dy", ".35em")
        .style("text-anchor", "end")
        .text(function(d) { return "Cluster " + d; });
    }

    function charger2()
    {
        var jsonStr = $("#json_str2").text();

        var data = jQuery.parseJSON(jsonStr.replace(/&quot;/g,'"'));

        //console.log(data);

        var width = 1200,
          height = 1200;

        var color = d3.scale.category20();

        var force = d3.layout.force()
          .charge(-120)
          .linkDistance(30)
          .size([width, height]);

        var svg = d3.select("#directed-load").append("svg")
          .attr("width", width)
          .attr("height", height);

        // d3.json("jsonForceDirected.json", function(error, graph) {
        // console.log(graph.nodes);
          force
            .nodes(data.nodes)
            .links(data.links)
            .start();

        var link = svg.selectAll(".link")
            .data(data.links)
          .enter().append("line")
            .attr("class", "link")
            .style("stroke-width", function(d) { return d.value/1000; });

        var node = svg.selectAll(".node")
            .data(data.nodes)
          .enter().append("circle")
            .attr("class", "node")
            .attr("r", 5)
            .style("fill", function(d) { return color(d.group); })
            .call(force.drag);

        node.append("title")
            .text(function(d) { return d.name; });

        force.on("tick", function() {
          link.attr("x1", function(d) { return d.source.x; })
              .attr("y1", function(d) { return d.source.y; })
              .attr("x2", function(d) { return d.target.x; })
              .attr("y2", function(d) { return d.target.y; });

          node.attr("cx", function(d) { return d.x; })
              .attr("cy", function(d) { return d.y; });
        });
    }

    function charger3()
    {
        var data_from_django = jQuery.parseJSON($("#data").text());
        //alert(data_from_django);
        var radius = 74,
            padding = 10;

        var color = d3.scale.ordinal()
            .range(["#98abc5", "#8a89a6"]);

        var arc = d3.svg.arc()
            .outerRadius(radius)
            .innerRadius(radius - 30);

        var pie = d3.layout.pie()
            .sort(null)
            .value(function(d) { return d.population; });

            data = data_from_django;

          color.domain(d3.keys(data[0]).filter(function(key) { return key !== "Cluster"; }));

          data.forEach(function(d) {
            d.ages = color.domain().map(function(name) {
              return {name: name, population: +d[name]};
            });
          });

          var legend = d3.select("#directed-load").append("svg")
              .attr("class", "legend")
              .attr("width", radius * 2)
              .attr("height", radius * 2)
            .selectAll("g")
              .data(color.domain().slice().reverse())
            .enter().append("g")
              .attr("transform", function(d, i) { return "translate(0," + i * 20 + ")"; });

          legend.append("rect")
              .attr("width", 18)
              .attr("height", 18)
              .style("fill", color);

          legend.append("text")
              .attr("x", 24)
              .attr("y", 9)
              .attr("dy", ".35em")
              .text(function(d) { return d; });

          var svg = d3.select("#directed-load").selectAll(".pie")
              .data(data)
            .enter().append("svg")
              .attr("class", "pie")
              .attr("width", radius * 2)
              .attr("height", radius * 2)
            .append("g")
              .attr("transform", "translate(" + radius + "," + radius + ")");

          svg.selectAll(".arc")
              .data(function(d) { return pie(d.ages); })
            .enter().append("path")
              .attr("class", "arc")
              .attr("d", arc)
              .style("fill", function(d) { return color(d.data.name); });

          svg.append("text")
              .attr("dy", ".35em")
              .style("text-anchor", "middle")
              .text(function(d) { return d.Cluster; });
    }

    charger1();
    charger2();
    charger3();
});