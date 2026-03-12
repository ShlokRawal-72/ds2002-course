// Task 2: use database
use bookstore

// Task 3: insert first author
db.authors.insertOne({
  "name": "Jane Austen",
  "nationality": "British",
  "bio": {
    "short": "English novelist known for novels about the British landed gentry.",
    "long": "Jane Austen was an English novelist whose works critique and comment upon the British landed gentry at the end of the 18th century. Her most famous novels include Pride and Prejudice, Sense and Sensibility, and Emma, celebrated for their wit, social commentary, and masterful character development."
  }
})

// Task 4: update to add birthday
db.authors.updateOne(
  { "name": "Jane Austen" },
  { $set: { "birthday": "1775-12-16" } }
)

// Task 5: insert four more authors
db.authors.insertMany([
  {
    "name": "Mark Twain",
    "nationality": "American",
    "birthday": "1835-11-30",
    "bio": {
      "short": "American writer, humorist, and essayist.",
      "long": "Known as the greatest humorist the United States has produced, famous for his novels The Adventures of Tom Sawyer and Adventures of Huckleberry Finn."
    }
  },
  {
    "name": "J.K. Rowling",
    "nationality": "British",
    "birthday": "1965-07-31",
    "bio": {
      "short": "British author and philanthropist.",
      "long": "Best known for writing the Harry Potter fantasy series, which has won multiple awards and sold over 500 million copies globally."
    }
  },
  {
    "name": "Haruki Murakami",
    "nationality": "Japanese",
    "birthday": "1949-01-12",
    "bio": {
      "short": "Japanese writer of novels, essays, and short stories.",
      "long": "His internationally translated body of work has garnered immense critical acclaim and numerous awards, featuring surrealistic and melancholic themes."
    }
  },
  {
    "name": "Agatha Christie",
    "nationality": "British",
    "birthday": "1890-09-15",
    "bio": {
      "short": "English writer known for her 66 detective novels.",
      "long": "Guinness World Records lists Christie as the best-selling fiction writer of all time, famous for her characters Hercule Poirot and Miss Marple."
    }
  }
])

// Task 6: total count
db.authors.countDocuments({})

// Task 7: British authors, sorted by name
db.authors.find({ "nationality": "British" }).sort({ "name": 1 })