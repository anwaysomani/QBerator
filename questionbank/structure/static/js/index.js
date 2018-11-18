myDiagram.nodeTemplate =
  $(go.Node, "Vertical", // second argument of a Node/Panel can be a Panel type
    /* set Node properties here */
    { // the Node.location point will be at the center of each node
      locationSpot: go.Spot.Center
    },

    /* add Bindings here */
    // example Node binding sets Node.location to the value of Node.data.loc
    new go.Binding("location", "loc"),

    /* add GraphObjects contained within the Node */
    // this Shape will be vertically above the TextBlock
    $(go.Shape,
      "RoundedRectangle", // string argument can name a predefined figure
      { /* set Shape properties here */ },
      // example Shape binding sets Shape.figure to the value of Node.data.fig
      new go.Binding("figure", "fig")),

    $(go.TextBlock,
      "default text",  // string argument can be initial text string
      { /* set TextBlock properties here */ },
      // example TextBlock binding sets TextBlock.text to the value of Node.data.key
      new go.Binding("text", "key"))
  );