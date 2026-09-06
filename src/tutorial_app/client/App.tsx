import { useEffect, useState } from 'react'
import './App.css'
import RecipeView, { type Recipe } from './RecipeView.tsx'

interface RecipeSummary {
  id: number
  name: string
}

function App() {
  const [recipes, setRecipes] = useState<RecipeSummary[]>([])
  const [selectedRecipe, setSelectedRecipe] = useState<Recipe | null>(null)
  const [selectedId, setSelectedId] = useState<number | null>(null)
  const [error, setError] = useState<string | null>(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const loadRecipes = async () => {
      try {
        const response = await fetch('/api/recipes')
        if (!response.ok) throw new Error('Unable to load recipes.')
        const data: RecipeSummary[] = await response.json()
        setRecipes(data)
        setSelectedId(data[0]?.id ?? null)
      } catch (loadError) {
        setError(loadError instanceof Error ? loadError.message : 'Unable to load recipes.')
      } finally {
        setLoading(false)
      }
    }

    void loadRecipes()
  }, [])

  useEffect(() => {
    if (selectedId === null) {
      setSelectedRecipe(null)
      return
    }

    const loadRecipe = async () => {
      setError(null)
      try {
        const response = await fetch(`/api/recipes/${selectedId}`)
        if (!response.ok) throw new Error('Unable to load that recipe.')
        setSelectedRecipe(await response.json() as Recipe)
      } catch (loadError) {
        setError(loadError instanceof Error ? loadError.message : 'Unable to load that recipe.')
      }
    }

    void loadRecipe()
  }, [selectedId])

  return (
    <main className="recipe-app">
      <header className="hero">
        <p className="eyebrow">A small kitchen notebook</p>
        <h1>Recipes worth repeating.</h1>
        <p className="intro">Simple ingredients, clear steps, and no fuss between you and dinner.</p>
      </header>

      <section className="recipe-layout" aria-label="Recipe browser">
        <nav className="recipe-list" aria-label="Recipes">
          <p className="section-label">Choose a recipe</p>
          {loading && <p className="muted">Loading recipes...</p>}
          {!loading && recipes.length === 0 && <p className="muted">No recipes yet.</p>}
          {recipes.map((recipe) => (
            <button
              className={recipe.id === selectedId ? 'recipe-link active' : 'recipe-link'}
              key={recipe.id}
              onClick={() => setSelectedId(recipe.id)}
              type="button"
            >
              <span>{recipe.name}</span>
              <span aria-hidden="true">-&gt;</span>
            </button>
          ))}
        </nav>

        <article className="recipe-panel">
          {error && <p className="error" role="alert">{error}</p>}
          {selectedRecipe ? <RecipeView recipe={selectedRecipe} /> : !error && <p className="muted">Select a recipe to begin.</p>}
        </article>
      </section>
    </main>
  )
}

export default App