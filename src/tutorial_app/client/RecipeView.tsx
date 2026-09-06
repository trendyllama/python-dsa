export interface Recipe {
  id: number
  name: string
  description: string | null
  ingredients: string[]
  instructions: string[]
}

function RecipeView({ recipe }: { recipe: Recipe }) {
  return (
    <div className="recipe-detail">
      <p className="section-label">Recipe {recipe.id.toString().padStart(2, '0')}</p>
      <h2>{recipe.name}</h2>
      {recipe.description && <p className="description">{recipe.description}</p>}
      <div className="recipe-columns">
        <section>
          <h3>Ingredients</h3>
          <ul>
            {recipe.ingredients.map((ingredient) => (
              <li key={ingredient}>{ingredient}</li>
            ))}
          </ul>
        </section>
        <section>
          <h3>Method</h3>
          <ol>
            {recipe.instructions.map((instruction, index) => (
              <li key={`${recipe.id}-${index}`}>{instruction}</li>
            ))}
          </ol>
        </section>
      </div>
    </div>
  )
}

export default RecipeView