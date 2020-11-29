(* ::Package:: *)

(*Aufgabe 2 a)*)
punkte = ListPointPlot3D[{{0,-1,2},{1,2,1},{0,0,2},{1,-1,1}},AxesLabel -> {x,y,z}, AxesOrigin->{0,0,0}]
(*Aufgabe 2 b)*)
(*(100)*)
ebene1 = Graphics3D[{Red, InfinitePlane[{{1, 0, 0}, {1, 10000000, 0}, {1, 0, 10000000}}]}];
(*(111)*)
ebene21 = Graphics3D[{Blue, InfinitePlane[{{1, 0, 0}, {0, 1, 0}, {0, 0, 1}}]}];
ebene22 = Graphics3D[{Blue, InfinitePlane[{{1, 1, 0}, {1, 0, 1}, {0, 1, 1}}]}];
(*(110)*)
ebene3 = Graphics3D[{Black, InfinitePlane[{{1, 0, 0}, {0, 1, 0}, {1, 0, 10000000}}]}];
(*(11-1)*)
ebene41 = Graphics3D[{Green, InfinitePlane[{{1, 0, 0}, {0, 1, 0}, {1, 1, 1}}]}];
ebene42 = Graphics3D[{Green, InfinitePlane[{{1, 0, 1}, {0, 1, 1}, {0, 0, 0}}]}];
(*(200)*)
ebene51 = Graphics3D[{Yellow, InfinitePlane[{{0.5, 0, 0}, {0.5, 1, 0}, {0.5, 0, 10000000}}]}];
ebene52 = Graphics3D[{Yellow, InfinitePlane[{{1, 0, 0}, {1, 1, 0}, {1, 0, 10000000}}]}];
(*(11-2)*)
ebene61 = Graphics3D[{Orange, InfinitePlane[{{1, 0, 0}, {0, 1, 0}, {1, 1, 0.5}}]}];
ebene62 = Graphics3D[{Orange, InfinitePlane[{{0, 0, 0}, {1, 0, 0.5}, {1, 1, 1}}]}];
ebene63 = Graphics3D[{Orange, InfinitePlane[{{0, 0, 0.5}, {1, 0, 1}, {0, 1, 1}}]}];

(*Zusammenf\[UDoubleDot]gen der Ebenen in Koordinatensystem mit Punkten*)
Show[punkte, ebene1, PlotRange -> All, AxesLabel -> {Style[x, FontSize->30], Style[y, FontSize->30], 
		Style[z, FontSize->30]}, AxesStyle -> 15, ViewPoint->{1,1,1}, AxesOrigin->{0,0,0}, 
		PlotLabel->Style["(100)", FontSize->25]]
Show[punkte, ebene21, ebene22, PlotRange -> All, 
		AxesLabel -> {Style[x, FontSize->30], Style[y, FontSize->30], Style[z, FontSize->30]}, 
		AxesStyle -> 15, ViewPoint->Left, AxesOrigin->{0,0,0}, PlotLabel->Style["(111)", FontSize->25]]
Show[punkte, ebene3, PlotRange -> All, 
		AxesLabel -> {Style[x, FontSize->30], Style[y, FontSize->30], Style[z, FontSize->30]}, 
		AxesStyle -> 15, ViewPoint->{1,1,1}, AxesOrigin->{0,0,0}, PlotLabel->Style["(110)", FontSize->25]]
Show[punkte, ebene41, ebene42, PlotRange -> All, 
		AxesLabel -> {Style[x, FontSize->30], Style[y, FontSize->30], Style[z, FontSize->30]}, 
		AxesStyle -> 15, ViewPoint->{2,0,0.5}, AxesOrigin->{0,0,0}, PlotLabel->Style["(11-1)", FontSize->25]]
Show[punkte, ebene51, ebene52, 
		PlotRange -> All, AxesLabel -> {Style[x, FontSize->30], Style[y, FontSize->30], Style[z, FontSize->30]}, 
		AxesStyle -> 15, ViewPoint->{1,1,1}, AxesOrigin->{0,0,0}, PlotLabel->Style["(200)", FontSize->25]]
Show[punkte, ebene61, ebene62, ebene63, PlotRange -> All, 
		AxesLabel -> {Style[x, FontSize->30], Style[y, FontSize->30], Style[z, FontSize->30]}, 
		AxesStyle -> 15, ViewPoint->{3,0,1}, AxesOrigin->{0,0,0}, PlotLabel->Style["(11-2)", FontSize->25]]


(* ::InheritFromParent:: *)
(**)


(*Aufgabe 2 c)*)
(*(210)*)
ebene71 = Graphics3D[{Brown, InfinitePlane[{{1/2, 0, 0}, {0, 1, 0}, {0, 1, 10000000}}]}];
ebene72 = Graphics3D[{Brown, InfinitePlane[{{2/2, 0, 0}, {0, 2, 0}, {0, 2, 10000000}}]}];

(*(420)*)
ebene81 = Graphics3D[{Pink, InfinitePlane[{{1/4, 0, 0}, {0, 1/2, 0}, {0, 1/2, 10000000}}]}];
ebene82 = Graphics3D[{Pink, InfinitePlane[{{2/4, 0, 0}, {0, 2/2, 0}, {0, 2/2, 10000000}}]}];
ebene83 = Graphics3D[{Pink, InfinitePlane[{{3/4, 0, 0}, {0, 3/2, 0}, {0, 3/2, 10000000}}]}];
ebene84 = Graphics3D[{Pink, InfinitePlane[{{4/4, 0, 0}, {0, 4/2, 0}, {0, 4/2, 10000000}}]}];

(*(630)*)
ebene91 = Graphics3D[{Gray, InfinitePlane[{{1/6, 0, 0}, {0, 1/3, 0}, {0, 1/3, 10000000}}]}];
ebene92 = Graphics3D[{Gray, InfinitePlane[{{2/6, 0, 0}, {0, 2/3, 0}, {0, 2/3, 10000000}}]}];
ebene93 = Graphics3D[{Gray, InfinitePlane[{{3/6, 0, 0}, {0, 3/3, 0}, {0, 3/3, 10000000}}]}];
ebene94 = Graphics3D[{Gray, InfinitePlane[{{4/6, 0, 0}, {0, 4/3, 0}, {0, 4/3, 10000000}}]}];
ebene95 = Graphics3D[{Gray, InfinitePlane[{{5/6, 0, 0}, {0, 5/3, 0}, {0, 5/3, 10000000}}]}];
ebene96 = Graphics3D[{Gray, InfinitePlane[{{6/6, 0, 0}, {0, 6/3, 0}, {0, 6/3, 10000000}}]}];
ebene97 = Graphics3D[{Gray, InfinitePlane[{{7/6, 0, 0}, {0, 7/3, 0}, {0, 7/3, 10000000}}]}];
ebene98 = Graphics3D[{Gray, InfinitePlane[{{8/6, 0, 0}, {0, 8/3, 0}, {0, 8/3, 10000000}}]}];

(*Zusammenf\[UDoubleDot]gen der Ebenen in Koordinatensystem mit Punkten*)
Show[punkte, ebene71, ebene72, PlotRange -> All, 
		AxesLabel -> {Style[x, FontSize->30], Style[y, FontSize->30], Style[z, FontSize->30]}, 
		AxesStyle -> 15, ViewPoint->Top, AxesOrigin->{0,0,0}, PlotLabel->Style["(210)", FontSize->25]]
Show[punkte, ebene81, ebene82, ebene83, ebene84, 
		PlotRange -> All, AxesLabel -> {Style[x, FontSize->30], Style[y, FontSize->30], Style[z, FontSize->30]}, 
		AxesStyle -> 15, ViewPoint->Top, AxesOrigin->{0,0,0}, PlotLabel->Style["(420)", FontSize->25]]
Show[punkte, ebene91, ebene92, ebene93, ebene94, ebene95, ebene95, ebene96, ebene97, ebene98, 
		PlotRange -> All, AxesLabel -> {Style[x, FontSize->30], Style[y, FontSize->30], Style[z, FontSize->30]}, 
		AxesStyle -> 15, ViewPoint->Top, AxesOrigin->{0,0,0}, PlotLabel->Style["(630)", FontSize->25]]


(* ::InheritFromParent:: *)
(**)


(* ::InheritFromParent:: *)
(**)


(* ::InheritFromParent:: *)
(**)
