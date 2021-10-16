package net.project.feemanagement.dao;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import net.project.feemanagemet.model.User;

public class UserDAO {
	
	private String jdbcURL= "jdbc:mysql://localhost:3306/student";
	private String jdbcUsername = "root";
	private String jdbcPassword = "password";
	
	private static final String INSERT_USERS_SQL = "INSERT INTO users "+"(name, amount, state) VALUES" + "(?, ?, ?);";
	private static final String SELECT_USER_BY_ID="select id, name, amount , state from users where id = ?";
	private static final String SELECT_ALL_USERS="select * from users";
	private static final String DELETE_USERS_SQL="delete from users where id = ?;";
	private static final String UPDATE_USERS_SQL="update users set name = ?, amount = ?, state = ?, where id = ?;";
	
	protected Connection getConnection() {
		Connection connection = null;
		
		try {
			Class.forName("com.mysql.jdbc.Driver");
			connection= DriverManager.getConnection(jdbcURL, jdbcUsername, jdbcPassword);
		} catch (ClassNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return connection;
	}
	public void insertUser(User user) throws SQLException {
		try(Connection connection = getConnection(); 
					PreparedStatement pst = connection.prepareStatement(INSERT_USERS_SQL)){
			pst.setString(1,user.getName());
			pst.setString(2,user.getAmount());
			pst.setString(3,user.getState());
			pst.executeUpdate();
			}catch(Exception e) {
			e.printStackTrace();
		}
	}
	public boolean updateUser(User user) throws SQLException {
		boolean rowUpdated;
		try(Connection connection = getConnection(); 
					PreparedStatement pst = connection.prepareStatement(UPDATE_USERS_SQL)){
			pst.setString(1,user.getName());
			pst.setString(2,user.getAmount());
			pst.setString(3,user.getState());
			pst.executeUpdate();
			pst.setInt(4,user.getId());
			
			rowUpdated = pst.executeUpdate() > 0;
		
		}
		return rowUpdated;
	}
	
	public User selectUser(int id) throws SQLException {
		
		User user= null;
		try(Connection connection = getConnection();
				PreparedStatement pst= connection.prepareStatement(SELECT_USER_BY_ID);){
			pst.setInt(1, id);
			System.out.println(pst);
			ResultSet rs= pst.executeQuery();
			
			while(rs.next()) {
				String name  = rs.getString("name");
				String amount= rs.getString("amount");
				String state = rs.getString("State");
				user = new User(id, name, amount, state);
			}
		}
			catch(SQLException e) {
				e.printStackTrace();
			}
			return user;
		
	}
	
public List<User> selectAllUser() throws SQLException {
		List<User> users = new ArrayList<>();
	
		try(Connection connection = getConnection();
				PreparedStatement pst= connection.prepareStatement(SELECT_ALL_USERS);){
			System.out.println(pst);
			ResultSet rs= pst.executeQuery();
			
			while(rs.next()) {
				int id = rs.getInt("id");
				String name  = rs.getString("name");
				String amount   = rs.getString("amount");
				String state = rs.getString("State");
				users.add(new User(id, name, amount, state));
			}
		}
			catch(SQLException e) {
				e.printStackTrace();
			}
			return users;
		
	}

public boolean deleteUser(int id) throws SQLException{
	boolean rowDeleted;
	try(Connection connection = getConnection();
			PreparedStatement pst= connection.prepareStatement(DELETE_USERS_SQL);){
		pst.setInt(1, id);
		rowDeleted = pst.executeUpdate() > 0;
	}
	return rowDeleted;
	}

}
	


