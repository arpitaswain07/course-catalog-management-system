
function SearchBar({ searchTerm, setSearchTerm }) {
    return (
        <section className="search-container">
            <input
                type="text"
                value={searchTerm}
                onChange={(event) => setSearchTerm(event.target.value)}
                placeholder="Search courses by name, instructor, or description..."
                aria-label="Search courses"
            />
        </section>
    );
}

export default SearchBar;
