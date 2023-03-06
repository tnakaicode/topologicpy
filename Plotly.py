import topologicpy
import topologic
import plotly
import plotly.graph_objects as go
from topologicpy.Vertex import Vertex
from topologicpy.Edge import Edge
from topologicpy.Wire import Wire
from topologicpy.Face import Face
from topologicpy.Cell import Cell
from topologicpy.CellComplex import CellComplex
from topologicpy.Cluster import Cluster
from topologicpy.Topology import Topology

class Plotly:
    @staticmethod
    def Colors():
        """
        Returns the list of named CSS colors that plotly can use.

        Returns
        -------
        list
            The list of named CSS colors.
        """
        return ["aliceblue","antiquewhite","aqua",
                "aquamarine","azure","beige",
                "bisque","black","blanchedalmond",
                "blue","blueviolet","brown",
                "burlywood","cadetblue",
                "chartreuse","chocolate",
                "coral","cornflowerblue","cornsilk",
                "crimson","cyan","darkblue",
                "darkcyan","darkgoldenrod","darkgray",
                "darkgrey","darkgreen","darkkhaki",
                "darkmagenta","darkolivegreen","darkorange",
                "darkorchid","darkred","darksalmon",
                "darkseagreen","darkslateblue","darkslategray",
                "darkslategrey","darkturquoise","darkviolet",
                "deeppink","deepskyblue","dimgray",
                "dimgrey","dodgerblue","firebrick",
                "floralwhite","forestgreen","fuchsia",
                "gainsboro","ghostwhite","gold",
                "goldenrod","gray","grey",
                "green"," greenyellow","honeydew",
                "hotpink","indianred","indigo",
                "ivory","khaki","lavender",
                "lavenderblush","lawngreen","lemonchiffon",
                "lightblue","lightcoral","lightcyan",
                "lightgoldenrodyellow","lightgray","lightgrey",
                "lightgreen","lightpink","lightsalmon",
                "lightseagreen","lightskyblue","lightslategray",
                "lightslategrey","lightsteelblue","lightyellow",
                "lime","limegreen","linen",
                "magenta","maroon","mediumaquamarine",
                "mediumblue","mediumorchid","mediumpurple",
                "mediumseagreen","mediumslateblue","mediumspringgreen",
                "mediumturquoise","mediumvioletred","midnightblue",
                "mintcream","mistyrose","moccasin",
                "navajowhite","navy","oldlace",
                "olive","olivedrab","orange",
                "orangered","orchid","palegoldenrod",
                "palegreen","paleturquoise","palevioletred",
                "papayawhip","peachpuff","peru",
                "pink","plum","powderblue",
                "purple","red","rosybrown",
                "royalblue","rebeccapurple","saddlebrown",
                "salmon","sandybrown","seagreen",
                "seashell","sienna","silver",
                "skyblue","slateblue","slategray",
                "slategrey","snow","springgreen",
                "steelblue","tan","teal",
                "thistle","tomato","turquoise",
                "violet","wheat","white",
                "whitesmoke","yellow","yellowgreen"]


    @staticmethod
    def DataByGraph(graph, vertexColor="white", vertexSize=6, vertexLabelKey=None, vertexGroupKey=None, vertexGroups=[], showVertices=True, edgeColor="black", edgeWidth=1, edgeLabelKey=None, edgeGroupKey=None, edgeGroups=[], showEdges=True):
        """
        Creates plotly vertex and edge data from the input graph.

        Parameters
        ----------
        graph : topologic.Graph
            The input graph.
        vertexLabelKey : str , optional
            The dictionary key to use to display the vertex label. The default is None.
        vertexGroupKey : str , optional
            The dictionary key to use to display the vertex group. The default is None.
        edgeLabelKey : str , optional
            The dictionary key to use to display the edge label. The default is None.
        edgeGroupKey : str , optional
            The dictionary key to use to display the edge group. The default is None.
        edgeColor : str , optional
            The desired color of the output edges. This can be any plotly color string and may be specified as:
            - A hex string (e.g. '#ff0000')
            - An rgb/rgba string (e.g. 'rgb(255,0,0)')
            - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
            - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
            - A named CSS color.
            The default is "black".
        edgeWidth : float , optional
            The desired thickness of the output edges. The default is 1.
        vertexColor : str , optional
            The desired color of the output vertices. This can be any plotly color string and may be specified as:
            - A hex string (e.g. '#ff0000')
            - An rgb/rgba string (e.g. 'rgb(255,0,0)')
            - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
            - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
            - A named CSS color.
            The default is "black".
        vertexSize : float , optional
            The desired size of the vertices. The default is 1.1.
        showEdges : bool , optional
            If set to True the edges will be drawn. Otherwise, they will not be drawn. The default is True.
        showVertices : bool , optional
            If set to True the vertices will be drawn. Otherwise, they will not be drawn. The default is True.

        Returns
        -------
        list
            The vertex and edge data list.

        """
        from topologicpy.Vertex import Vertex
        from topologicpy.Edge import Edge
        from topologicpy.Dictionary import Dictionary
        from topologicpy.Topology import Topology
        from topologicpy.Graph import Graph
        import plotly.graph_objs as go

        if not isinstance(graph, topologic.Graph):
            return None
        v_labels = []
        v_groupList = []
        data = []
        if showVertices:
            vertices = Graph.Vertices(graph)
            if vertexLabelKey or vertexGroupKey:
                for v in vertices:
                    Xn=[Vertex.X(v) for v in vertices] # x-coordinates of nodes
                    Yn=[Vertex.Y(v) for v in vertices] # y-coordinates of nodes
                    Zn=[Vertex.Z(v) for v in vertices] # x-coordinates of nodes
                    v_label = ""
                    v_group = ""
                    d = Topology.Dictionary(v)
                    if d:
                        try:
                            v_label = str(Dictionary.ValueAtKey(d, key=vertexLabelKey)) or ""
                        except:
                            v_label = ""
                        try:
                            v_group = str(Dictionary.ValueAtKey(d, key=vertexGroupKey)) or ""
                        except:
                            v_group = ""
                    try:
                        v_groupList.append(vertexGroups.index(v_group))
                    except:
                        v_groupList.append(len(vertexGroups))
                    if not v_label == "" and not v_group == "":
                        v_label = v_label+" ("+v_group+")"
                    v_labels.append(v_label)
            else:
                for v in vertices:
                    Xn=[Vertex.X(v) for v in vertices] # x-coordinates of nodes
                    Yn=[Vertex.Y(v) for v in vertices] # y-coordinates of nodes
                    Zn=[Vertex.Z(v) for v in vertices] # x-coordinates of nodes
            if len(list(set(v_groupList))) < 2:
                v_groupList = vertexColor
            if len(v_labels) < 1:
                v_labels = ""
            v_trace=go.Scatter3d(x=Xn,
                y=Yn,
                z=Zn,
                mode='markers',
                name='Graph Vertices',
                legendgroup=4,
                legendrank=4,
                marker=dict(symbol='circle',
                                size=vertexSize,
                                color=v_groupList,
                                colorscale='Viridis',
                                line=dict(color=edgeColor, width=0.5)
                                ),
                text=v_labels,
                hoverinfo='text'
                )
            data.append(v_trace)
        
        if showEdges:
            Xe=[]
            Ye=[]
            Ze=[]
            e_labels = []
            e_groupList = []
            edges = Graph.Edges(graph)
                
            if edgeLabelKey or edgeGroupKey:
                for e in edges:
                    sv = Edge.StartVertex(e)
                    ev = Edge.EndVertex(e)
                    Xe+=[Vertex.X(sv),Vertex.X(ev), None] # x-coordinates of edge ends
                    Ye+=[Vertex.Y(sv),Vertex.Y(ev), None] # y-coordinates of edge ends
                    Ze+=[Vertex.Z(sv),Vertex.Z(ev), None] # z-coordinates of edge ends
                    e_label = ""
                    e_group = ""
                    d = Topology.Dictionary(e)
                    if d:
                        try:
                            e_label = str(Dictionary.ValueAtKey(d, key=edgeLabelKey)) or ""
                        except:
                            e_label = ""
                        try:
                            e_group = str(Dictionary.ValueAtKey(d, key=edgeGroupKey)) or ""
                        except:
                            e_group = ""
                    try:
                        e_groupList.append(edgeGroups.index(e_group))
                    except:
                        e_groupList.append(len(edgeGroups))
                    if not e_label == "" and not e_group == "":
                        e_label = e_label+" ("+e_group+")"
                    e_labels.append(e_label)
            else:
                for e in edges:
                    sv = Edge.StartVertex(e)
                    ev = Edge.EndVertex(e)
                    Xe+=[Vertex.X(sv),Vertex.X(ev), None] # x-coordinates of edge ends
                    Ye+=[Vertex.Y(sv),Vertex.Y(ev), None] # y-coordinates of edge ends
                    Ze+=[Vertex.Z(sv),Vertex.Z(ev), None] # z-coordinates of edge ends

            if len(list(set(e_groupList))) < 2:
                e_groupList = edgeColor
            if len(e_labels) < 1:
                e_labels = ""
            
            e_trace=go.Scatter3d(x=Xe,
                                 y=Ye,
                                 z=Ze,
                                 mode='lines',
                                 name='Graph Edges',
                                 legendgroup=5,
                                 legendrank=5,
                                 line=dict(color=e_groupList, width=edgeWidth),
                                 text=e_labels,
                                 hoverinfo='text'
                                )
            data.append(e_trace)

        return data

    @staticmethod
    def DataByTopology(topology, vertexLabelKey=None, vertexGroupKey=None, edgeLabelKey=None, edgeGroupKey=None, faceLabelKey=None, faceGroupKey=None, vertexGroups=[], edgeGroups=[], faceGroups=[], faceColor="white", faceOpacity=0.5, edgeColor="black", edgeWidth=1, vertexColor="black", vertexSize=1.1, showFaces=True, showEdges=True, showVertices=True, verticesLabel="Topology Vertices", edgesLabel="Topology Edges", facesLabel="Topology Faces"):
        """
        Creates plotly face, edge, and vertex data.

        Parameters
        ----------
        topology : topologic.Topology
            The input topology. This must contain faces and or edges.
        vertexLabelKey : str , optional
            The dictionary key to use to display the vertex label. The default is None.
        vertexGroupKey : str , optional
            The dictionary key to use to display the vertex group. The default is None.
        edgeLabelKey : str , optional
            The dictionary key to use to display the edge label. The default is None.
        edgeGroupKey : str , optional
            The dictionary key to use to display the edge group. The default is None.
        faceLabelKey : str , optional
            The dictionary key to use to display the face label. The default is None.
        faceGroupKey : str , optional
            The dictionary key to use to display the face group. The default is None.
        vertexGroups : list , optional
            The list of vertex groups against which to index the color of the vertex. The default is [].
        edgeGroups : list , optional
            The list of edge groups against which to index the color of the edge. The default is [].
        faceGroups : list , optional
            The list of face groups against which to index the color of the face. The default is [].
        faceColor : str , optional
            The desired color of the output faces. This can be any plotly color string and may be specified as:
            - A hex string (e.g. '#ff0000')
            - An rgb/rgba string (e.g. 'rgb(255,0,0)')
            - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
            - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
            - A named CSS color.
            The default is "white".
        faceOpacity : float , optional
            The desired opacity of the output faces (0=transparent, 1=opaque). The default is 0.5.
        edgeColor : str , optional
            The desired color of the output edges. This can be any plotly color string and may be specified as:
            - A hex string (e.g. '#ff0000')
            - An rgb/rgba string (e.g. 'rgb(255,0,0)')
            - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
            - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
            - A named CSS color.
            The default is "black".
        edgeWidth : float , optional
            The desired thickness of the output edges. The default is 1.
        vertexColor : str , optional
            The desired color of the output vertices. This can be any plotly color string and may be specified as:
            - A hex string (e.g. '#ff0000')
            - An rgb/rgba string (e.g. 'rgb(255,0,0)')
            - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
            - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
            - A named CSS color.
            The default is "black".
        vertexSize : float , optional
            The desired size of the vertices. The default is 1.1.
        showFaces : bool , optional
            If set to True the faces will be drawn. Otherwise, they will not be drawn. The default is True.
        showEdges : bool , optional
            If set to True the edges will be drawn. Otherwise, they will not be drawn. The default is True.
        showVertices : bool , optional
            If set to True the vertices will be drawn. Otherwise, they will not be drawn. The default is True.
        verticesLabel : str , optional
            The legend label string used to identify vertices. The default is "Topology Vertices".
        edgesLabel : str , optional
            The legend label string used to identify edges. The default is "Topology Edges".
        facesLabel : str , optional
            The legend label string used to idenitfy edges. The default is "Topology Faces".
        Returns
        -------
        list
            The vertex, edge, and face data list.

        """
        from topologicpy.Topology import Topology
        from topologicpy.Dictionary import Dictionary

        def vertexData(vertices, dictionaries=None, vertexColor="black", vertexSize=1.1, vertexLabelKey=None, vertexGroupKey=None, vertexGroups=[], verticesLabel="Topology Vertices"):
            x = []
            y = []
            z = []
            v_labels = []
            v_groupList = []
            v_label = ""
            v_group = ""
            if vertexLabelKey or vertexGroupKey:
                for m, v in enumerate(vertices):
                    x.append(v[0])
                    y.append(v[1])
                    z.append(v[2])
                    v_label = ""
                    v_group = ""
                    if len(dictionaries) > 0:
                        d = dictionaries[m]
                        if d:
                            try:
                                v_label = str(Dictionary.ValueAtKey(d, key=vertexLabelKey)) or ""
                            except:
                                v_label = ""
                            try:
                                v_group = str(Dictionary.ValueAtKey(d, key=vertexGroupKey)) or ""
                            except:
                                v_group = ""
                        try:
                            v_groupList.append(vertexGroups.index(v_group))
                        except:
                            v_groupList.append(len(vertexGroups))
                        if not v_label == "" and not v_group == "":
                            v_label = v_label+" ("+v_group+")"
                        v_labels.append(v_label)
            else:
                for v in vertices:
                    x.append(v[0])
                    y.append(v[1])
                    z.append(v[2])
            
            if len(list(set(v_groupList))) < 2:
                v_groupList = vertexColor
            if len(v_labels) < 1:
                v_labels = ""
            return go.Scatter3d(x=x,
                                y=y,
                                z=z,
                                name=verticesLabel,
                                showlegend=True,
                                marker=dict(color=v_groupList,  size=vertexSize),
                                mode='markers',
                                legendgroup=1,
                                legendrank=1,
                                text=v_labels,
                                hoverinfo='text',
                                hovertext=v_labels)

        def edgeData(vertices, edges, dictionaries=None, edgeColor="black", edgeWidth=1, edgeLabelKey=None, edgeGroupKey=None, edgeGroups=[], edgesLabel="Topology Edges"):
            x = []
            y = []
            z = []
            e_labels = []
            e_groupList = []
            e_label = ""
            if edgeLabelKey or edgeGroupKey:
                for m, e in enumerate(edges):
                    sv = vertices[e[0]]
                    ev = vertices[e[1]]
                    x+=[sv[0],ev[0], None] # x-coordinates of edge ends
                    y+=[sv[1],ev[1], None] # y-coordinates of edge ends
                    z+=[sv[2],ev[2], None] # z-coordinates of edge ends
                    e_label = ""
                    e_group = ""
                    if len(dictionaries) > 0:
                        d = dictionaries[m]
                        if d:
                            try:
                                e_label = str(Dictionary.ValueAtKey(d, key=edgeLabelKey)) or ""
                            except:
                                e_label = ""
                            try:
                                e_group = str(Dictionary.ValueAtKey(d, key=edgeGroupKey)) or ""
                            except:
                                e_group = ""
                        try:
                            e_groupList.append(edgeGroups.index(e_group))
                        except:
                            e_groupList.append(len(edgeGroups))
                        if not e_label == "" and not e_group == "":
                            e_label = e_label+" ("+e_group+")"
                        e_labels.append(e_label)
            else:
                for e in edges:
                    sv = vertices[e[0]]
                    ev = vertices[e[1]]
                    x+=[sv[0],ev[0], None] # x-coordinates of edge ends
                    y+=[sv[1],ev[1], None] # y-coordinates of edge ends
                    z+=[sv[2],ev[2], None] # z-coordinates of edge ends
                
            if len(list(set(e_groupList))) < 2:
                    e_groupList = edgeColor
            if len(e_labels) < 1:
                e_labels = ""
            return go.Scatter3d(x=x,
                                y=y,
                                z=z,
                                name=edgesLabel,
                                showlegend=True,
                                marker_size=0,
                                mode="lines",
                                line=dict(color=e_groupList, width=edgeWidth),
                                legendgroup=2,
                                legendrank=2,
                                text=e_labels,
                                hoverinfo='text')


        def faceData(vertices, faces, dictionaries=None, faceColor="white", faceOpacity=0.5, faceLabelKey=None, faceGroupKey=None, faceGroups=[]):
            x = []
            y = []
            z = []
            intensities = []
            for v in vertices:
                x.append(v[0])
                y.append(v[1])
                z.append(v[2])
                intensities.append(0)
            i = []
            j = []
            k = []
            f_labels = []
            f_groupList = []
            if faceLabelKey or faceGroupKey:
                for m, f in enumerate(faces):
                    i.append(f[0])
                    j.append(f[1])
                    k.append(f[2])
                    f_label = ""
                    f_group = ""
                    if len(dictionaries) > 0:
                        d = dictionaries[m]
                        if d:
                            try:
                                f_label = str(Dictionary.ValueAtKey(d, key=faceLabelKey)) or ""
                            except:
                                f_label = ""
                            try:
                                f_group = str(Dictionary.ValueAtKey(d, key=faceGroupKey)) or ""
                            except:
                                f_group = ""
                        try:
                            f_groupList.append(faceGroups.index(f_group))
                        except:
                            f_groupList.append(len(faceGroups))
                        if not f_label == "" and not f_group == "":
                            f_label = f_label+" ("+f_group+")"
                        f_labels.append(f_label)
            else:
                for f in faces:
                    i.append(f[0])
                    j.append(f[1])
                    k.append(f[2])
                
            if len(list(set(f_groupList))) < 2:
                    f_groupList = faceColor
            if len(f_labels) < 1:
                f_labels = ""
            return go.Mesh3d(
                    x=x,
                    y=y,
                    z=z,
                    # i, j and k give the vertices of triangles
                    # here we represent the 4 triangles of the tetrahedron surface
                    i=i,
                    j=j,
                    k=k,
                    name='Topology Faces',
                    showscale=False,
                    showlegend = True,
                    legendgroup=3,
                    legendrank=3,
                    color = f_groupList,
                    opacity = faceOpacity,
                    hoverinfo = 'text',
                    text=f_labels,
                    hovertext = f_labels,
                    flatshading = True,
                    lighting = {"facenormalsepsilon": 0},
                )
        from topologicpy.Cluster import Cluster
        from topologicpy.Topology import Topology
        from topologicpy.Dictionary import Dictionary
        if not isinstance(topology, topologic.Topology):
            return None

        if edgeLabelKey or edgeGroupKey:
            tp_edges = Topology.SubTopologies(topology, subTopologyType="edge")
            e_dictionaries = []
            for tp_edge in tp_edges:
                e_dictionaries.append(Topology.Dictionary(tp_edge))
        else:
            e_dictionaries = None
        if faceLabelKey or faceGroupKey:
            tp_faces = Topology.SubTopologies(topology, subTopologyType="face")
            f_dictionaries = []
            for tp_face in tp_faces:
                f_dictionaries.append(Topology.Dictionary(tp_face))
        else:
           f_dictionaries = None
        
        #geometry = Topology.Geometry(topology)
        #vertices = geometry['vertices']
        #edges = geometry['edges']
        #faces = geometry['faces']
        data = []
        tp_verts = Topology.SubTopologies(topology, subTopologyType="vertex")
        vertices = []
        v_dictionaries = []
        for tp_v in tp_verts:
            vertices.append([tp_v.X(), tp_v.Y(), tp_v.Z()])
            if vertexLabelKey or vertexGroupKey:
                v_dictionaries.append(Topology.Dictionary(tp_v))
        if showVertices:
            data.append(vertexData(vertices, dictionaries=v_dictionaries, vertexColor=vertexColor, vertexSize=vertexSize, vertexLabelKey=vertexLabelKey, vertexGroupKey=vertexGroupKey, vertexGroups=vertexGroups))
        if showEdges and topology.Type() > topologic.Vertex.Type():
            tp_edges = Topology.SubTopologies(topology, subTopologyType="edge")
            edges = []
            for tp_edge in tp_edges:
                sv = Edge.StartVertex(tp_edge)
                si = Vertex.Index(sv, tp_verts)
                ev = Edge.EndVertex(tp_edge)
                ei = Vertex.Index(ev, tp_verts)
                edges.append([si, ei])
            data.append(edgeData(vertices, edges, dictionaries=[], edgeColor=edgeColor, edgeWidth=edgeWidth, edgeLabelKey=edgeLabelKey, edgeGroupKey=edgeGroupKey, edgeGroups=edgeGroups, edgesLabel=edgesLabel))
        if showFaces and topology.Type() >= topologic.Face.Type():
            tp_faces = Topology.SubTopologies(topology, subTopologyType="face")
            triangles = []
            f_dictionaries = []
            for tp_face in tp_faces:
                temp_faces = Face.Triangulate(tp_face)
                #temp_faces = [tp_face]
                for tri in temp_faces:
                    triangles.append(tri)
                    if faceLabelKey or faceGroupKey:
                        f_dictionaries.append(Topology.Dictionary(tp_face))
            faces = []
            for tri in triangles:
                w = Face.ExternalBoundary(tri)
                w_vertices = Topology.SubTopologies(w, subTopologyType="vertex")
                temp_f = []
                for w_v in w_vertices:
                    i = Vertex.Index(vertex=w_v, vertices=tp_verts, tolerance=0.01)
                    temp_f.append(i)
                faces.append(temp_f)
            data.append(faceData(vertices, faces, dictionaries=f_dictionaries, faceColor=faceColor, faceOpacity=faceOpacity, faceLabelKey=faceLabelKey, faceGroupKey=faceGroupKey, faceGroups=faceGroups))
            #data.append(vertexData(vertices, dictionaries=[], vertexColor=vertexColor, vertexSize=5, vertexLabelKey=vertexLabelKey, vertexGroupKey=vertexGroupKey, vertexGroups=vertexGroups))
        return data

    @staticmethod
    def FigureByConfusionMatrix(matrix,
             categories=[],
             minValue=None,
             maxValue=None,
             title="Confusion Matrix",
             xTitle = "Actual",
             yTitle = "Predicted",
             width=950,
             height=500,
             showScale = True,
             colorScale='Viridis',
             colorSamples=10,
             backgroundColor='rgba(0,0,0,0)',
             marginLeft=0,
             marginRight=0,
             marginTop=40,
             marginBottom=0):
        """
        Returns a Plotly Figure of the input confusion matrix. Actual categories are displayed on the X-Axis, Predicted categories are displayed on the Y-Axis.

        Parameters
        ----------
        matrix : list
            The matrix to display.
        categories : list
            The list of categories to use on the X and Y axes.
        minValue : float , optional
            The desired minimum value to use for the color scale. If set to None, the minmum value found in the input matrix will be used. The default is None.
        maxValue : float , optional
            The desired maximum value to use for the color scale. If set to None, the maximum value found in the input matrix will be used. The default is None.
        title : str , optional
            The desired title to display. The default is "Confusion Matrix".
        xTitle : str , optional
            The desired X-axis title to display. The default is "Actual".
        yTitle : str , optional
            The desired Y-axis title to display. The default is "Predicted".
        width : int , optional
            The desired width of the figure. The default is 950.
        height : int , optional
            The desired height of the figure. The default is 500.
        showScale : bool , optional
            If set to True, a color scale is shown on the right side of the figure. The default is True.
        colorScale : str , optional
            The desired type of plotly color scales to use (e.g. "Viridis", "Plasma"). The default is "Viridis". For a full list of names, see https://plotly.com/python/builtin-colorscales/.
        colorSamples : int , optional
            The number of discrete color samples to use for displaying the data. The default is 10.
        backgroundColor : str , optional
            The desired background color. This can be any plotly color string and may be specified as:
            - A hex string (e.g. '#ff0000')
            - An rgb/rgba string (e.g. 'rgb(255,0,0)')
            - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
            - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
            - A named CSS color.
            The default is 'rgba(0,0,0,0)' (transparent).
        marginLeft : int , optional
            The desired left margin in pixels. The default is 0.
        marginRight : int , optional
            The desired right margin in pixels. The default is 0.
        marginTop : int , optional
            The desired top margin in pixels. The default is 40.
        marginBottom : int , optional
            The desired bottom margin in pixels. The default is 0.

        """
        #import plotly.figure_factory as ff
        import plotly.graph_objects as go
        import plotly.express as px

        annotations = []

        # Transpose the confusion matrix
        matrix = matrix.T
        colors = px.colors.sample_colorscale(colorScale, [n/(colorSamples -1) for n in range(colorSamples)])
        if not minValue:
            minValue = 0
        if not maxValue:
            max_values = []
            for i, row in enumerate(matrix):
                max_values.append(max(row))
                for j, value in enumerate(row):
                    annotations.append(
                        {
                            "x": categories[j],
                            "y": categories[i],
                            "font": {"color": "black"},
                            "bgcolor": "white",
                            "opacity": 0.5,
                            "text": str(round(value,2)), 
                            "xref": "x1",
                            "yref": "y1",
                            "showarrow": False
                        }
                    )
            maxValue = max(max_values)
        else:
            for i, row in enumerate(matrix):
                for j, value in enumerate(row):
                    annotations.append(
                        {
                            "x": categories[j],
                            "y": categories[i],
                            "font": {"color": "black"},
                            "bgcolor": "white",
                            "opacity": 0.5,
                            "text": str(round(value,2)),
                            "xref": "x1",
                            "yref": "y1",
                            "showarrow": False
                        }
                    )
        data = go.Heatmap(z=matrix, y=categories, x=categories, zmin=minValue, zmax=maxValue, showscale=showScale, colorscale=colors)
        
        layout = {
            "width": width,
            "height": height,
            "title": title,
            "xaxis": {"title": xTitle},
            "yaxis": {"title": yTitle},
            "annotations": annotations,
            "paper_bgcolor": backgroundColor,
            "plot_bgcolor": backgroundColor,
            "margin":dict(l=marginLeft, r=marginRight, t=marginTop, b=marginBottom)
        }
        fig = go.Figure(data=data, layout=layout)
        return fig
        
    @staticmethod
    def FigureByDataFrame(df,
             labels=[],
             title="Untitled",
             x_title="X Axis",
             x_spacing=1.0,
             y_title="Y Axis",
             y_spacing=1,
             use_markers=False,
             chart_type="Line"):
        """
        Returns a Plotly Figure of the input dataframe

        Parameters
        ----------
        df : pandas.df
            The p[andas dataframe to display.
        data_labels : list
            The labels to use for the data.
        title : str , optional
            The chart title. The default is "Untitled".
        x_title : str , optional
            The X-axis title. The default is "Epochs".
        x_spacing : float , optional
            The X-axis spacing. The default is 1.0.
        y_title : str , optional
            The Y-axis title. The default is "Accuracy and Loss".
        y_spacing : float , optional
            THe Y-axis spacing. The default is 0.1.
        use_markers : bool , optional
            If set to True, markers will be displayed. The default is False.
        chart_type : str , optional
            The desired type of chart. The options are "Line", "Bar", or "Scatter". It is case insensitive. The default is "Line".
        renderer : str , optional
            The desired plotly renderer. The default is "notebook".

        Returns
        -------
        None.

        """
        import plotly.express as px
        if chart_type.lower() == "line":
            fig = px.line(df, x=labels[0], y=labels[1:], title=title, markers=use_markers)
        elif chart_type.lower() == "bar":
            fig = px.bar(df, x=labels[0], y=labels[1:], title=title)
        elif chart_type.lower() == "scatter":
            fig = px.scatter(df, x=labels[0], y=labels[1:], title=title)
        else:
            raise NotImplementedError
        fig.layout.xaxis.title=x_title
        fig.layout.xaxis.dtick=x_spacing
        fig.layout.yaxis.title=y_title
        fig.layout.yaxis.dtick= y_spacing
        return fig

    @staticmethod
    def FigureByData(data, color=None, width=950, height=500, xAxis=False, yAxis=False, zAxis=False, axisSize=1, backgroundColor='rgba(0,0,0,0)', marginLeft=0, marginRight=0, marginTop=20, marginBottom=0):
        """
        Creates a plotly figure.

        Parameters
        ----------
        data : list
            The input list of plotly data.
        width : int , optional
            The width in pixels of the figure. The default value is 950.
        height : int , optional
            The height in pixels of the figure. The default value is 950.
        xAxis : bool , optional
            If set to True the x axis is drawn. Otherwise it is not drawn. The default is False.
        yAxis : bool , optional
            If set to True the y axis is drawn. Otherwise it is not drawn. The default is False.
        zAxis : bool , optional
            If set to True the z axis is drawn. Otherwise it is not drawn. The default is False.
        axisSize : float , optional
            The size of the X,Y,Z, axes. The default is 1.
        backgroundColor : str , optional
            The desired color of the background. This can be any plotly color string and may be specified as:
            - A hex string (e.g. '#ff0000')
            - An rgb/rgba string (e.g. 'rgb(255,0,0)')
            - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
            - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
            - A named CSS color.
            The default is "rgba(0,0,0,0)".
        marginLeft : int , optional
            The size in pixels of the left margin. The default value is 0.
        marginRight : int , optional
            The size in pixels of the right margin. The default value is 0.
        marginTop : int , optional
            The size in pixels of the top margin. The default value is 20.
        marginBottom : int , optional
            The size in pixels of the bottom margin. The default value is 0.
        
        Returns
        -------
        plotly.graph_objs._figure.Figure
            The created plotly figure.

        """
        from topologicpy.Vertex import Vertex
        from topologicpy.Edge import Edge
        from topologicpy.Wire import Wire
        if not isinstance(data, list):
            return None

        v0 = Vertex.ByCoordinates(0,0,0)
        v1 = Vertex.ByCoordinates(axisSize,0,0)
        v2 = Vertex.ByCoordinates(0,axisSize,0)
        v3 = Vertex.ByCoordinates(0,0,axisSize)

        if xAxis:
            xEdge = Edge.ByVertices([v0,v1])
            xWire = Wire.ByEdges([xEdge])
            xData = Plotly.DataByTopology(xWire, edgeColor="red", edgeWidth=6, showFaces=False, showEdges=True, showVertices=False, edgesLabel="X-Axis")
            data = data + xData
        if yAxis:
            yEdge = Edge.ByVertices([v0,v2])
            yWire = Wire.ByEdges([yEdge])
            yData = Plotly.DataByTopology(yWire, edgeColor="green", edgeWidth=6, showFaces=False, showEdges=True, showVertices=False, edgesLabel="Y-Axis")
            data = data + yData
        if zAxis:
            zEdge = Edge.ByVertices([v0,v3])
            zWire = Wire.ByEdges([zEdge])
            zData = Plotly.DataByTopology(zWire, edgeColor="blue", edgeWidth=6, showFaces=False, showEdges=True, showVertices=False, edgesLabel="Z-Axis")
            data = data + zData

        figure = go.Figure(data=data)
        figure.update_layout(
            width=width,
            height=height,
            showlegend=True,
            scene = dict(
                xaxis = dict(visible=False),
                yaxis = dict(visible=False),
                zaxis =dict(visible=False),
                ),
            scene_aspectmode='data',
            paper_bgcolor=backgroundColor,
            plot_bgcolor=backgroundColor,
            margin=dict(l=marginLeft, r=marginRight, t=marginTop, b=marginBottom),
            )
        return figure

    @staticmethod
    def FigureByPieChart(data, values, names):
        """
        Creates a plotly pie chart figure.

        Parameters
        ----------
        data : list
            The input list of plotly data.
        values : list
            The input list of values.
        names : list
            The input list of names.
        """
        import pandas as pd
        import plotly.express as px
        dlist = list(map(list, zip(*data)))
        df = pd.DataFrame(dlist, columns=data['names'])
        fig = px.pie(df, values=values, names=names)
        return fig
    
    @staticmethod
    def SetCamera(figure, camera=[1.25, 1.25, 1.25], target=[0, 0, 0], up=[0, 0, 1]):
        """
        Sets the camera for the input figure.

        Parameters
        ----------
        figure : plotly.graph_objs._figure.Figure
            The input plotly figure.
        camera : list , optional
            The desired location of the camera. The default is [0,0,0].
        target : list , optional
            The desired camera target. The default is [0,0,0].
        up : list , optional
            The desired up vector. The default is [0,0,1].
        
        Returns
        -------
        plotly.graph_objs._figure.Figure
            The updated figure

        """
        if not isinstance(camera, list):
            return None
        if not isinstance(target, list):
            return None
        if not isinstance(up, list):
            return None
        scene_camera = dict(
        up=dict(x=up[0], y=up[1], z=up[2]),
        eye=dict(x=camera[0], y=camera[1], z=camera[2]),
        center=dict(x=target[0], y=target[1], z=target[2])
        )
        figure.update_layout(scene_camera=scene_camera)
        return figure

    @staticmethod
    def Show(figure, camera=[1.25, 1.25, 1.25], renderer="notebook", target=[0, 0, 0], up=[0, 0, 1]):
        """
        Shows the input figure.

        Parameters
        ----------
        figure : plotly.graph_objs._figure.Figure
            The input plotly figure.
        camera : list , optional
            The desired location of the camera. The default is [0,0,0].
        renderer : str , optional
            The desired rendered. See Plotly.Renderers(). The default is "notebook".
        target : list , optional
            The desired camera target. The default is [0,0,0].
        up : list , optional
            The desired up vector. The default is [0,0,1].
        
        Returns
        -------
        None
            
        """
        if not isinstance(figure, plotly.graph_objs._figure.Figure):
            return None
        if not renderer.lower() in Plotly.Renderers():
            return None
        figure = Plotly.SetCamera(figure, camera=camera, target=target, up=up)
        figure.show(renderer=renderer)
        return None

    @staticmethod
    def Renderers():
        """
        Returns a list of the available plotly renderers.

        Parameters
        ----------
        
        Returns
        -------
        list
            The list of the available plotly renderers.

        """
        return ['plotly_mimetype', 'jupyterlab', 'nteract', 'vscode',
         'notebook', 'notebook_connected', 'kaggle', 'azure', 'colab',
         'cocalc', 'databricks', 'json', 'png', 'jpeg', 'jpg', 'svg',
         'pdf', 'browser', 'firefox', 'chrome', 'chromium', 'iframe',
         'iframe_connected', 'sphinx_gallery', 'sphinx_gallery_png']

    @staticmethod
    def ExportToImage(figure, path, format="png", width="1920", height="1080"):
        """
        Exports the plotly figure to an image.

        Parameters
        ----------
        figure : plotly.graph_objs._figure.Figure
            The input plotly figure.
        path : str
            The image file path.
        format : str , optional
            The desired format. This can be any of "jpg", "jpeg", "pdf", "png", "svg", or "webp". It is case insensitive. The default is "png". 
        width : int , optional
            The width in pixels of the figure. The default value is 1920.
        height : int , optional
            The height in pixels of the figure. The default value is 1080.
        
        Returns
        -------
        bool
            True if the image was exported sucessfully. False otherwise.

        """
        if not isinstance(figure, plotly.graph_objs._figure.Figure):
            return None
        if not isinstance(path, str):
            return None
        if not format.lower() in ["jpg", "jpeg", "pdf", "png", "svg", "webp"]:
            return None
        returnStatus = False
        try:
            plotly.io.write_image(figure, path, format=format.lower(), scale=None, width=width, height=height, validate=True, engine='auto')
            returnStatus = True
        except:
            returnStatus = False
        return returnStatus

