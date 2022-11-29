import I1M.BusquedaPrimeroElMejor
import Data.Array

type Posicion = (Int,Int)
type Tablero  = Array Int Posicion

inicial8P :: Tablero 
inicial8P = array (0,8) [(2,(1,3)),(6,(2,3)),(3,(3,3)),
                         (5,(1,2)),(0,(2,2)),(4,(3,2)),
                         (1,(1,1)),(7,(2,1)),(8,(3,1))]
final8P :: Tablero
final8P = array (0,8) [(1,(1,3)),(2,(2,3)),(3,(3,3)),
                       (8,(1,2)),(0,(2,2)),(4,(3,2)),
                       (7,(1,1)),(6,(2,1)),(5,(3,1))]

distancia :: Posicion -> Posicion -> Int
distancia (x1,y1) (x2,y2) = abs (x1-x2) + abs (y1-y2)

adyacente :: Posicion -> Posicion -> Bool
adyacente p1 p2 = distancia p1 p2 == 1

todosMovimientos :: Tablero -> [Tablero]
todosMovimientos t = 
    [t//[(0,t!i),(i,t!0)] | i<-[1..8], 
                            adyacente (t!0) (t!i)] 

data Tableros = Est [Tablero] deriving Show
sucesores8P :: Tableros -> [Tableros]
sucesores8P (Est(n@(t:ts))) = 
    [Est (t':n) | t' <- todosMovimientos t, 
                  t' `notElem` ts]

esFinal8P :: Tableros -> Bool
esFinal8P (Est (t:_)) = t == final8P

heur1 :: Tablero  -> Int
heur1 t = 
    sum [distancia (t!i) (final8P!i) | i <- [0..8]]

instance Eq Tableros
    where Est(t1:_) == Est(t2:_) = heur1 t1 == heur1 t2

instance Ord Tableros where 
    Est (t1:_) <= Est (t2:_) = heur1 t1 <= heur1 t2

buscaPM_8P = buscaPM sucesores8P      
                     esFinal8P        
                     (Est [inicial8P])